from PySide6.QtWidgets import (
    QMainWindow,
    QPushButton,
    QFileDialog,
    QMessageBox,
    QLabel,
    QComboBox,
    QListWidget,
    QListWidgetItem,
    QWidget,
    QVBoxLayout,
)
from ui_py.ui_mainwindow import Ui_MainWindow
from PySide6.QtCore import QUrl, QEvent, QSize, QThread, QPropertyAnimation, QEasingCurve, QTimer, Qt, QObject, Signal
from PySide6.QtGui import QDesktopServices, QMovie, QPixmap, QIcon
from ui_py.ui_settings import Ui_MainWindow as Ui_SettingsWindow
from pathlib import Path
from urllib.request import Request, urlopen
import os
import sys
import json
import yt_dlp
from controlroom.themes import get_mainwindow_stylesheet, get_settings_stylesheet


def _configure_ssl_cert_bundle():
    try:
        import certifi
    except ImportError:
        return

    cert_path = certifi.where()
    if cert_path:
        os.environ.setdefault("SSL_CERT_FILE", cert_path)
        os.environ.setdefault("REQUESTS_CA_BUNDLE", cert_path)


def _user_config_dir():
    if sys.platform.startswith("win"):
        base_dir = os.environ.get("APPDATA")
        if not base_dir:
            base_dir = Path.home() / "AppData" / "Roaming"
        return Path(base_dir) / "Cozydownloader"

    if sys.platform == "darwin":
        return Path.home() / "Library" / "Application Support" / "Cozydownloader"

    base_dir = os.environ.get("XDG_CONFIG_HOME")
    if base_dir:
        return Path(base_dir) / "Cozydownloader"
    return Path.home() / ".config" / "Cozydownloader"


def _is_running_from_source():
    # In source/dev mode (for example, running from VS Code), keep config local to project.
    if getattr(sys, "frozen", False):
        return False
    if os.environ.get("VSCODE_PID"):
        return True
    return True


def _effective_config_dir():
    if _is_running_from_source():
        return Path(__file__).resolve().parents[1] / "config"
    return _user_config_dir()


def _app_root_dir():
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent
    return Path(__file__).resolve().parents[1]


def _resolve_ffmpeg_location():
    app_root = _app_root_dir()
    candidates = [
        app_root / "ffmpeg" / "bin",
        app_root / "ffmpeg",
    ]

    executable_names = ["ffmpeg.exe", "ffmpeg"]
    for candidate in candidates:
        for executable_name in executable_names:
            if (candidate / executable_name).exists():
                return candidate
    return None







class ScalableButton(QPushButton):
    """Custom button that scales up on hover."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.default_icon_size = None
        self.hover_icon_size = None
        
    def set_scaling(self, default_size, hover_size):
        """Set the icon sizes for normal and hover states."""
        self.default_icon_size = default_size
        self.hover_icon_size = hover_size
        self.setIconSize(self.default_icon_size)
    
    def enterEvent(self, event):
        """Scale up icon on hover."""
        if self.hover_icon_size:
            self.setIconSize(self.hover_icon_size)
        super().enterEvent(event)
    
    def leaveEvent(self, event):
        """Scale down icon when not hovering."""
        if self.default_icon_size:
            self.setIconSize(self.default_icon_size)
        super().leaveEvent(event)


















class settingsWindow(QMainWindow):
    sleep_time_changed = Signal(int)
    cookies_enabled_changed = Signal(bool)
    gui_mode_changed = Signal(bool)
    settings_saved = Signal(dict)

    def __init__(self, background_selected_callback=None):
        super().__init__()

        self.ui = Ui_SettingsWindow()
        self.ui.setupUi(self)
        
        # Replace the generated checkboxes with animated toggles
        self._replace_with_animated_toggles()

        self.pending_background_path = None
        self.save_settings_bt = None
        self._create_save_button()
        
        self.background_selected_callback = background_selected_callback
        self.ui.Upload_bt.clicked.connect(self.select_background_file)
        self.ui.sleeptime__int.valueChanged.connect(self._on_sleep_time_value_changed)
        self.save_settings_bt.clicked.connect(self._save_all_settings)

        self._load_settings_into_controls()
        self._apply_theme()

    def _replace_with_animated_toggles(self):
        """Animate the existing checkbox toggles in place without replacing them."""
        self._toggle_knobs = {}
        self._toggle_animations = {}

        self._setup_existing_toggle(self.ui.pushButton)
        self._setup_existing_toggle(self.ui.pushButton_2)

    def _setup_existing_toggle(self, toggle):
        toggle.setText("")
        toggle.setCursor(Qt.CursorShape.PointingHandCursor)
        toggle.setFixedSize(52, 28)
        toggle.setStyleSheet(
            "QCheckBox::indicator {"
            "width: 52px;"
            "height: 28px;"
            "background: transparent;"
            "border: none;"
            "}"
        )

        knob = QLabel(toggle)
        knob.setFixedSize(20, 20)
        knob.setStyleSheet("background-color: white; border-radius: 10px;")
        knob.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents, True)
        knob.show()

        animation = QPropertyAnimation(knob, b"pos", self)
        animation.setDuration(180)
        animation.setEasingCurve(QEasingCurve.Type.InOutCubic)

        self._toggle_knobs[toggle] = knob
        self._toggle_animations[toggle] = animation

        toggle.toggled.connect(lambda checked, current_toggle=toggle: self._animate_existing_toggle(current_toggle, checked))
        self._sync_existing_toggle(toggle)

    def _sync_existing_toggle(self, toggle):
        checked = toggle.isChecked()
        self._update_existing_toggle_style(toggle, checked)
        knob = self._toggle_knobs[toggle]
        knob.move(self._toggle_knob_target_x(toggle, checked), (toggle.height() - knob.height()) // 2)

    def _toggle_knob_target_x(self, toggle, checked):
        knob = self._toggle_knobs[toggle]
        if checked:
            return toggle.width() - knob.width() - 4
        return 4

    def _update_existing_toggle_style(self, toggle, checked):
        if checked:
            toggle.setStyleSheet(
                "QCheckBox {"
                "background-color: rgb(52, 132, 255);"
                "border: 2px solid rgb(122, 178, 255);"
                "border-radius: 14px;"
                "}"
                "QCheckBox::indicator {"
                "width: 52px;"
                "height: 28px;"
                "background: transparent;"
                "border: none;"
                "}"
            )
        else:
            toggle.setStyleSheet(
                "QCheckBox {"
                "background-color: rgb(120, 120, 120);"
                "border: 2px solid rgba(255, 255, 255, 190);"
                "border-radius: 14px;"
                "}"
                "QCheckBox::indicator {"
                "width: 52px;"
                "height: 28px;"
                "background: transparent;"
                "border: none;"
                "}"
            )

    def _animate_existing_toggle(self, toggle, checked):
        if toggle not in self._toggle_knobs:
            return

        knob = self._toggle_knobs[toggle]
        animation = self._toggle_animations[toggle]
        self._update_existing_toggle_style(toggle, checked)

        target_pos = knob.pos()
        target_pos.setX(self._toggle_knob_target_x(toggle, checked))

        animation.stop()
        animation.setStartValue(knob.pos())
        animation.setEndValue(target_pos)
        animation.start()

    def _app_base_dir(self):
        if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
            return Path(sys._MEIPASS)
        return Path(__file__).resolve().parents[1]

    def _assets_dir(self):
        return self._app_base_dir() / "assets"

    def _config_dir(self):
        return _effective_config_dir()

    def _bundled_config_dir(self):
        return self._app_base_dir() / "config"

    def _create_save_button(self):
        self.save_settings_bt = QPushButton("Save settings", self.ui.centralwidget)
        self.save_settings_bt.setObjectName("saveSettings_bt")
        self.save_settings_bt.setMinimumSize(QSize(0, 40))
        self.ui.verticalLayout.insertWidget(2, self.save_settings_bt)

    def _configfile_path(self):
        return self._config_dir() / "background_settings.json"

    def _bundled_configfile_path(self):
        return self._bundled_config_dir() / "background_settings.json"

    def _read_settings_data(self):
        for config_path in (self._configfile_path(), self._bundled_configfile_path()):
            if not config_path.exists():
                continue

            try:
                with config_path.open("r", encoding="utf-8") as config_file:
                    loaded = json.load(config_file)
                return loaded if isinstance(loaded, dict) else {}
            except (json.JSONDecodeError, OSError):
                continue

        return {}

    def _update_settings_data(self, updates):
        if not isinstance(updates, dict):
            return False

        config_dir = self._config_dir()
        config_dir.mkdir(parents=True, exist_ok=True)

        config_data = self._read_settings_data()
        config_data.update(updates)

        try:
            with self._configfile_path().open("w", encoding="utf-8") as config_file:
                json.dump(config_data, config_file, indent=2)
            return True
        except OSError:
            return False

    def _save_background_path(self, selected_path):
        config_data = self._read_settings_data()
        is_light_mode_enabled = self._coerce_bool(config_data.get("gui_mode_enabled", False), default=False)
        return self._update_settings_data({
            self._background_path_key(is_light_mode_enabled): selected_path,
            "home_background_path": selected_path,
        })

    def _coerce_non_negative_int(self, value, default=0):
        try:
            return max(0, int(value))
        except (TypeError, ValueError):
            return int(default)

    def _coerce_bool(self, value, default=False):
        if value is None:
            return bool(default)
        if isinstance(value, str):
            return value.strip().lower() in {"1", "true", "yes", "on"}
        return bool(value)

    def _load_settings_into_controls(self):
        config_data = self._read_settings_data()
        is_light_mode_enabled = self._coerce_bool(config_data.get("gui_mode_enabled", False), default=False)

        self.ui.sleeptime__int.setValue(
            self._coerce_non_negative_int(config_data.get("default_sleep_seconds", 0), default=0)
        )
        self.ui.pushButton.setChecked(self._coerce_bool(config_data.get("cookies_enabled", False), default=False))
        self.ui.pushButton_2.setChecked(is_light_mode_enabled)

        raw_background_path = self._background_path_for_mode(config_data, is_light_mode_enabled)
        self.pending_background_path = raw_background_path or None
        self.pending_background_is_light_mode = is_light_mode_enabled

    def _current_settings_payload(self):
        config_data = self._read_settings_data()
        is_light_mode_enabled = bool(self.ui.pushButton_2.isChecked())
        pending_mode_matches_current = getattr(self, "pending_background_is_light_mode", is_light_mode_enabled) == is_light_mode_enabled
        if self.pending_background_path and pending_mode_matches_current:
            background_path = self.pending_background_path
        else:
            background_path = self._background_path_for_mode(config_data, is_light_mode_enabled)

        return {
            "default_sleep_seconds": self._sleep_time_from_input(),
            "cookies_enabled": self._cookies_enabled_input(),
            "gui_mode_enabled": is_light_mode_enabled,
            self._background_path_key(is_light_mode_enabled): background_path,
            "home_background_path": background_path,
        }

    def _set_saved_feedback(self):
        self.save_settings_bt.setText("Saved")
        self.save_settings_bt.setEnabled(False)
        QTimer.singleShot(900, self._reset_save_button_text)

    def _reset_save_button_text(self):
        self.save_settings_bt.setText("Save settings")
        self.save_settings_bt.setEnabled(True)

    def _read_sleep_time_from_settings(self):
        config_data = self._read_settings_data()
        raw_value = config_data.get("default_sleep_seconds", 0)
        return self._coerce_non_negative_int(raw_value, default=0)

    def _save_sleep_time(self, sleep_seconds):
        return self._update_settings_data({"default_sleep_seconds": int(sleep_seconds)})
    
    def _save_cookies_enabled(self, enabled):
        return self._update_settings_data({"cookies_enabled": bool(enabled)})

    def _save_gui_mode_enabled(self, enabled):
        return self._update_settings_data({"gui_mode_enabled": bool(enabled)})

    def _background_path_key(self, is_light_mode_enabled):
        return "home_background_path_light" if is_light_mode_enabled else "home_background_path_dark"

    def _background_path_for_mode(self, config_data, is_light_mode_enabled):
        mode_key = self._background_path_key(is_light_mode_enabled)
        mode_path = str(config_data.get(mode_key, "")).strip()
        if mode_path:
            return mode_path

        legacy_path = str(config_data.get("home_background_path", "")).strip()
        return legacy_path

    def _sleep_time_from_input(self):
        # Commit any in-progress typed text before reading current spinbox value.
        self.ui.sleeptime__int.interpretText()
        return self._coerce_non_negative_int(self.ui.sleeptime__int.value(), default=0)
    
    def _cookies_enabled_input(self):
        return self.ui.pushButton.isChecked()

    def _on_sleep_time_value_changed(self, value):
        # Keep value normalized in memory; persistence happens through Save settings.
        self._coerce_non_negative_int(value, default=0)
    
    def _on_cookies_toggled(self, checked):
        self._save_cookies_enabled(checked)

    def _set_failed_feedback(self):
        self.save_settings_bt.setText("Save failed")
        self.save_settings_bt.setEnabled(False)
        QTimer.singleShot(1300, self._reset_save_button_text)

    def _save_all_settings(self):
        settings_payload = self._current_settings_payload()
        # Write all settings atomically in a single JSON update to avoid partial updates and race conditions.
        write_ok = self._update_settings_data(settings_payload)

        if not write_ok:
            self._set_failed_feedback()
            return

        self.sleep_time_changed.emit(settings_payload["default_sleep_seconds"])
        self.cookies_enabled_changed.emit(settings_payload["cookies_enabled"])
        self.gui_mode_changed.emit(settings_payload["gui_mode_enabled"])
        self.settings_saved.emit(settings_payload)

        selected_background = settings_payload.get("home_background_path", "")
        if selected_background and self.background_selected_callback:
            self.background_selected_callback(selected_background)

        # Apply the theme to the settings window itself
        self.changeuiStyle()
        self._set_saved_feedback()

    def select_background_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Home Background",
            str(Path.home()),
            "Image Files (*.png *.jpg *.jpeg *.bmp *.webp *.gif)",
        )

        if not file_path:
            return

        self.pending_background_path = file_path
        self.pending_background_is_light_mode = self._coerce_bool(self.ui.pushButton_2.isChecked(), default=False)
        self.ui.BackgroundLabel.setText(Path(file_path).name)

    def activatecookies(self):
        return self._cookies_enabled_input()

    def setdefaultsleep(self):
        return self._sleep_time_from_input()

    def _apply_theme(self):
        """Apply the current theme mode to the settings window."""
        is_light_mode_enabled = self._coerce_bool(
            self._read_settings_data().get("gui_mode_enabled", False),
            default=False
        )
        # Convert light mode flag to dark mode flag for stylesheet function
        is_dark_mode = not is_light_mode_enabled
        self.setStyleSheet(get_settings_stylesheet(is_dark_mode))

    def changeuiStyle(self):
        """Apply the theme based on the GUI mode toggle and emit signal."""
        is_light_mode_enabled = bool(self.ui.pushButton_2.isChecked())
        # Convert light mode flag to dark mode flag for stylesheet function
        is_dark_mode = not is_light_mode_enabled
        self.setStyleSheet(get_settings_stylesheet(is_dark_mode))
        self.gui_mode_changed.emit(is_light_mode_enabled)












class DownloadWorker(QObject):
    success = Signal(object)
    error = Signal(str)
    done = Signal()

    def __init__(self, url, ydl_opts):
        super().__init__()
        self.url = url
        self.ydl_opts = ydl_opts

    def run(self):
        try:
            with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
                download_result = ydl.extract_info(self.url, download=True)
            self.success.emit(download_result)
        except Exception as exc:
            self.error.emit(str(exc))
        finally:
            self.done.emit()


class PreviewInfoWorker(QObject):
    success = Signal(object)
    error = Signal(str)
    done = Signal()

    def __init__(self, url, ydl_opts):
        super().__init__()
        self.url = url
        self.ydl_opts = ydl_opts

    def run(self):
        try:
            with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
                info = ydl.extract_info(self.url, download=False)
            self.success.emit(info)
        except Exception as exc:
            self.error.emit(str(exc))
        finally:
            self.done.emit()













class MainController(QMainWindow):
    def __init__(self): #the intializer for the main window, sets the buttons connections and values for variabs
        super().__init__()

        _configure_ssl_cert_bundle()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Default bundled backgrounds used when no saved settings exist yet.
        self.default_background_by_mode = {
            False: Path("assets/StarfieldSimulation004.gif"),
            True: Path("assets/stzk3syjhin41.gif"),
        }

        # hide the settings page till clicked
        self.settings_window = None
        self.page_background_movies = {}
        self.sleep_time_seconds = self._load_saved_sleep_time()
        self.has_cookies = self._load_saved_cookies_enabled()
        self.is_light_mode_enabled = self._load_saved_theme()

        # Render user-selected media behind selected stacked pages.
        self.page_background_labels = {
            self.ui.pageHome: QLabel(self.ui.pageHome),
            self.ui.pageInputPreview: QLabel(self.ui.pageInputPreview),
            self.ui.page_downloads: QLabel(self.ui.page_downloads),
        }
        for background_label in self.page_background_labels.values():
            background_label.setScaledContents(True)
            background_label.setStyleSheet("border: none; margin: 0px; padding: 0px;")
            background_label.lower()
            background_label.hide()

        # Defer initial resize until layout is finalized
        QTimer.singleShot(100, self._resize_page_background_labels)

        # Keep button space reserved in the layout even when hidden.
        button_policy = self.ui.CheckURL_bt.sizePolicy()
        button_policy.setRetainSizeWhenHidden(True)
        self.ui.CheckURL_bt.setSizePolicy(button_policy)

        # Connect signals
        self.ui.CheckURL_bt.clicked.connect(self.process_input)
        self.ui.URL_placement.textChanged.connect(self.update_checkurl_visibility)
        self.ui.URL_placement.textChanged.connect(self.sync_user_input_preview)
        self.ui.backHome_bt.clicked.connect(self.go_home_page)
        self.ui.home_kudopage_bt.clicked.connect(self.go_home_page)
        self.ui.kuddos_bt.clicked.connect(self.go_page_three)
        self.ui.goPage3_bt.clicked.connect(self.open_ytdlp_github)
        self.ui.link_button.clicked.connect(self.open_our_github)
        self.ui.Downloads_BT.clicked.connect(self.go_downloadspage)
        self.ui.BackHome_Downloads.clicked.connect(self.go_home_page)
        self.ui.Settings_BT.clicked.connect(self.go_settings_window)
        self.ui.stackedWidget.currentChanged.connect(self._on_stacked_page_changed)

        # Keep original VideoInfo label prefixes and append loaded metadata to them.
        self.video_info_label_prefixes = {
            self.ui.label: self.ui.label.text(),
            self.ui.label_10: self.ui.label_10.text(),
            self.ui.label_9: self.ui.label_9.text(),
            self.ui.label_8: self.ui.label_8.text(),
        }
        self._reset_video_info_labels()

        # Animate Settings button icon with spinning gif while hovered.
        self._setup_settings_hover_gif()

        # Keep selected URL while user configures download options on preview page.
        self.pending_url = ""
        self.pending_is_playlist = False
        self.current_playlist_entries = []
        self.download_thread = None
        self.download_worker = None
        self.preview_thread = None
        self.preview_worker = None
        self.current_preview_thumbnail_pixmap = None
        self.download_history_records = []
        self.download_thumbnail_cache = {}

        # Configure preview controls for download mode/settings.
        self._setup_preview_download_controls()
        self._setup_download_history_ui()
        self._load_download_history_records()

        # Add hover scaling to icon buttons
        self._add_hover_scaling(self.ui.goPage3_bt, QSize(50, 55), QSize(58, 63), duration=150)
        self._add_hover_scaling(self.ui.kuddos_bt, QSize(28, 27), QSize(34, 36), duration=150)

        # Page 2 shows a preview of typed input from page 1.
        self.ui.userInput_le.setReadOnly(True)

        # Hide the button until there is text in the URL field.
        self.update_checkurl_visibility(self.ui.URL_placement.text())
        self.sync_user_input_preview(self.ui.URL_placement.text())

        # load the gif for secret page
        gif_path = self._assets_dir() / "starfall.gif"
        if not gif_path.exists():
            gif_path = self._project_base_dir() / "starfall.gif"
        self.loading_movie = QMovie(str(gif_path))
        self.ui.giflabel.setMovie(self.loading_movie)
        self.ui.giflabel.resize(self.ui.giflabel.size())
        self.ui.giflabel.setText("")

        if self.loading_movie.isValid():
            self.loading_movie.start()
        else:
            self.ui.giflabel.setText("GIF failed to load")

        self._apply_theme()
        
        self._apply_saved_home_background()
        
        # Apply the saved theme (dark mode is the default)








    def process_input(self):
        url = self.ui.URL_placement.text().strip()
        if not url:
            self._show_error_feedback("Please enter a valid URL.")
            return

        if self.preview_thread and self.preview_thread.isRunning():
            self._show_error_feedback("A URL check is already in progress.")
            return

        self.pending_url = url
        self.ui.imagePlaceholder_lb.clear()
        self.ui.imagePlaceholder_lb.setText("Loading thumbnail...")
        self._set_loading_video_info_labels()

        ydl_opts = {
            'outtmpl': '%(title)s.%(ext)s',
            'quiet': False,
            'no_warnings': False,
            'socket_timeout': 20,
            'extractor_retries': 1,
        }

        self.preview_thread = QThread(self)
        self.preview_worker = PreviewInfoWorker(url, ydl_opts)
        self.preview_worker.moveToThread(self.preview_thread)

        self.preview_thread.started.connect(self.preview_worker.run)
        self.preview_worker.success.connect(self._on_preview_info_success)
        self.preview_worker.error.connect(self._on_preview_info_error)
        self.preview_worker.done.connect(self._on_preview_info_done)
        self.preview_worker.done.connect(self.preview_thread.quit)
        self.preview_worker.done.connect(self.preview_worker.deleteLater)
        self.preview_thread.finished.connect(self.preview_thread.deleteLater)

        self.ui.CheckURL_bt.setEnabled(False)
        self.ui.CheckURL_bt.setText("Checking...")
        self.preview_thread.start()

    def _on_preview_info_success(self, info):
        self._set_preview_thumbnail_from_info(info)
        self._set_video_info_labels_from_info(info)
        self._update_playlist_detection_state(info)
        self._populate_playlist_thumbnail_browser(info)
        self.preview_download_bt.setVisible(True)
        # Navigate only after URL metadata loads successfully.
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageInputPreview)

    def _on_preview_info_error(self, error_text):
        self.pending_is_playlist = False
        self._set_playlist_scope_controls_for_link_type(False, 0)
        self._populate_playlist_thumbnail_browser(None)
        self._reset_video_info_labels()
        self.preview_download_bt.setVisible(False)
        self._show_error_feedback(f"Failed to read URL details:\n{error_text}")

    def _on_preview_info_done(self):
        self.ui.CheckURL_bt.setText("Download")
        self.ui.CheckURL_bt.setEnabled(True)
        self.preview_worker = None
        self.preview_thread = None

    def _setup_preview_download_controls(self):
        self.ui.label_2.setText("Download mode")
        self.ui.label_3.setText("Container")
        self.ui.label_5.setText("Resolution")

        self.ui.comboBox.clear()
        self.ui.comboBox.addItems(["Video + Audio", "Audio only"])

        self.ui.comboBox_3.clear()
        self.ui.comboBox_3.addItems(["480p", "720p", "1080p", "1440p"])
        self.ui.comboBox_3.setCurrentText("1080p")

        # Hide unused placeholder controls from the generated UI.
        self.ui.label_4.hide()
        self.ui.lineEdit.hide()
        self.ui.label_6.hide()
        self.ui.lineEdit_2.hide()
        self.ui.lineEdit_3.hide()

        # Use playlist controls defined in the .ui file so they can be edited in Designer.
        self.playlist_type_label = self.ui.playlistType_lb
        self.playlist_type_value = self.ui.playlistTypeValue_lb
        self.playlist_scope_label = self.ui.playlistScope_lb
        self.playlist_scope_combo = self.ui.playlistScope_cb
        self.playlist_scope_combo.setItemData(0, "single")
        self.playlist_scope_combo.setItemData(1, "playlist")
        self.playlist_scope_combo.setCurrentIndex(0)
        self._set_playlist_scope_controls_for_link_type(False, 0)

        # Use playlist browser widgets from .ui and apply runtime behavior only.
        self.playlist_browser_widget = self.ui.playlistBrowserWid
        self.playlist_browser_label = self.ui.playlistBrowserTitle_lb
        self.playlist_thumbnail_list = self.ui.playlistThumbs_lw
        self.playlist_thumbnail_list.setViewMode(QListWidget.ViewMode.IconMode)
        self.playlist_thumbnail_list.setFlow(QListWidget.Flow.LeftToRight)
        self.playlist_thumbnail_list.setWrapping(False)
        self.playlist_thumbnail_list.setResizeMode(QListWidget.ResizeMode.Adjust)
        self.playlist_thumbnail_list.setMovement(QListWidget.Movement.Static)
        self.playlist_thumbnail_list.setIconSize(QSize(120, 68))
        self.playlist_thumbnail_list.setGridSize(QSize(150, 96))
        self.playlist_thumbnail_list.setSpacing(6)
        self.playlist_thumbnail_list.setUniformItemSizes(True)
        self.playlist_thumbnail_list.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.playlist_thumbnail_list.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.playlist_thumbnail_list.itemSelectionChanged.connect(self._on_playlist_thumbnail_selected)
        self.playlist_browser_widget.hide()

        # Use the button defined in Designer and keep it hidden until metadata is loaded.
        self.preview_download_bt = self.ui.previewDownload_bt
        self.preview_download_bt.setVisible(False)
        self._setup_preview_download_hover_effect()
        self._setup_download_button_feedback()

        self.ui.comboBox.currentTextChanged.connect(self._on_download_mode_changed)
        self.preview_download_bt.clicked.connect(self.download_with_selected_options)

        # Defaults: 1080p and best audio-video quality.
        self.ui.comboBox.setCurrentText("Video + Audio")
        self._on_download_mode_changed(self.ui.comboBox.currentText())

    def _on_download_mode_changed(self, mode_text):
        self.ui.comboBox_2.clear()

        if mode_text == "Audio only":
            self.ui.comboBox_2.addItems(["mp3", "mkv"])
            self.ui.comboBox_2.setCurrentText("mp3")
        else:
            self.ui.comboBox_2.addItems(["mp4", "mkv", "webm", "mov"])
            self.ui.comboBox_2.setCurrentText("mp4")

    def _build_ydl_options_from_selection(self):
        mode_text = self.ui.comboBox.currentText()
        container = self.ui.comboBox_2.currentText().lower().strip()
        resolution_text = self.ui.comboBox_3.currentText().lower().strip()
        resolution = int(resolution_text.replace("p", ""))
        scope = self.playlist_scope_combo.currentData() if hasattr(self, "playlist_scope_combo") else "single"
        sleeptime = max(0, int(self.sleep_time_seconds))
        ydl_opts = {
            'outtmpl': '%(title)s.%(ext)s',
            'quiet': False,
            'no_warnings': False,
            # Default behavior: download only the URL's current video unless user chose full playlist.
            'noplaylist': scope != 'playlist',
        }

        ffmpeg_location = _resolve_ffmpeg_location()
        if ffmpeg_location is not None:
            ydl_opts['ffmpeg_location'] = str(ffmpeg_location)

        if sleeptime > 0:
            # Use a fixed sleep interval between requests.
            ydl_opts['min_sleep_interval'] = sleeptime
            ydl_opts['max_sleep_interval'] = sleeptime

        if self.has_cookies:
            detected_browser = self._detect_cookies_browser()
            if detected_browser:
                ydl_opts['cookiesfrombrowser'] = (detected_browser,)

        if mode_text == "Audio only":
            ydl_opts['format'] = 'bestaudio/best'
            if container == 'mp3':
                ydl_opts['postprocessors'] = [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '0',
                }]
            elif container == 'mkv':
                ydl_opts['postprocessors'] = [{
                    'key': 'FFmpegVideoRemuxer',
                    'preferredformat': 'mkv',
                }]
        else:
            if container == 'mp4':
                ydl_opts['format'] = f'bestvideo[height<={resolution}]+bestaudio[ext=m4a]/best[height<={resolution}]'
            else:
                ydl_opts['format'] = f'bestvideo[height<={resolution}]+bestaudio/best[height<={resolution}]'

            if container == 'mp4':
                ydl_opts['merge_output_format'] = 'mp4'
            else:
                ydl_opts['postprocessors'] = [{
                    'key': 'FFmpegVideoRemuxer',
                    'preferredformat': container,
                }]

        return ydl_opts

    def download_with_selected_options(self):
        url = self.pending_url.strip()
        if not url:
            self._set_video_info_status("Error: Enter a URL first on Home page")
            return

        if self.download_thread and self.download_thread.isRunning():
            self._set_video_info_status("A download is already in progress")
            return

        destination_dir = QFileDialog.getExistingDirectory(
            self,
            "Select destination folder",
            str(Path.home()),
        )
        if not destination_dir:
            self._set_video_info_status("Download cancelled: no destination selected")
            return

        try:
            ydl_opts = self._build_ydl_options_from_selection()
            ydl_opts['outtmpl'] = str(Path(destination_dir) / '%(title)s.%(ext)s')
            if self.has_cookies and 'cookiesfrombrowser' not in ydl_opts:
                self._set_video_info_status("Downloading... (cookies enabled, no browser profile found)")
            else:
                self._set_video_info_status("Downloading...")

            self.download_thread = QThread(self)
            self.download_worker = DownloadWorker(url, ydl_opts)
            self.download_worker.moveToThread(self.download_thread)

            self.download_thread.started.connect(self.download_worker.run)
            self.download_worker.success.connect(self._on_download_worker_success)
            self.download_worker.error.connect(self._on_download_worker_error)
            self.download_worker.done.connect(self._on_download_worker_done)
            self.download_worker.done.connect(self.download_thread.quit)
            self.download_worker.done.connect(self.download_worker.deleteLater)
            self.download_thread.finished.connect(self.download_thread.deleteLater)

            self.preview_download_bt.setEnabled(False)
            self._set_download_button_busy(True)
            self.download_thread.start()
        except Exception as e:
            self._set_video_info_status(f"Error: {str(e)}")
            self._set_download_button_busy(False)
            self.preview_download_bt.setEnabled(True)

    def _on_download_worker_success(self, download_result):
        self._append_download_history(download_result)
        self._set_video_info_status("Download complete!")

    def _on_download_worker_error(self, error_text):
        self._set_video_info_status(f"Error: {error_text}")
        self._show_error_feedback(f"Download failed:\n{error_text}")

    def _on_download_worker_done(self):
        self._set_download_button_busy(False)
        self.preview_download_bt.setEnabled(True)
        self.download_worker = None
        self.download_thread = None

    def _setup_download_history_ui(self):


        # Reuse the Designer-defined list so placement/style stays editable in .ui.
        self.download_history_list = self.ui.downloadHistory_lw
        self.download_history_list.setViewMode(QListWidget.ViewMode.ListMode)
        self.download_history_list.setIconSize(QSize(120, 68))
        self.download_history_list.setSpacing(6)
        self.download_history_list.setWordWrap(True)
        self.download_history_list.setUniformItemSizes(False)
        self.download_history_list.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.download_history_list.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.download_history_list.itemSelectionChanged.connect(self._on_download_history_item_selected)

        self.download_thumbnail_placeholder = self.ui.Thumbnail_placeholder
        self.download_info_placeholder = self.ui.info_downloaded
        self.download_thumbnail_placeholder.setScaledContents(False)
        self.download_thumbnail_placeholder.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.download_thumbnail_placeholder.setText("Select a download")

    def _download_history_path(self):
        config_dir = self._config_dir()
        config_dir.mkdir(parents=True, exist_ok=True)
        return config_dir / "download_history.json"

    def _serialize_download_item(self, info):
        if not isinstance(info, dict):
            return None

        duration_seconds = info.get("duration")
        size_bytes = info.get("filesize") or info.get("filesize_approx")
        output_name = (
            info.get("_filename")
            or info.get("filepath")
            or info.get("filename")
            or info.get("requested_filename")
            or "Unknown file"
        )
        if output_name == "Unknown file":
            requested_downloads = info.get("requested_downloads")
            if isinstance(requested_downloads, list):
                for requested_download in requested_downloads:
                    if not isinstance(requested_download, dict):
                        continue
                    output_name = (
                        requested_download.get("filepath")
                        or requested_download.get("filename")
                        or requested_download.get("_filename")
                        or output_name
                    )
                    if output_name != "Unknown file":
                        break
        file_ext = info.get("ext") or Path(str(output_name)).suffix.lstrip(".")
        extractor_name = (
            info.get("extractor_key")
            or info.get("ie_key")
            or info.get("extractor")
            or info.get("_type")
            or ""
        )

        return {
            "title": info.get("title") or "Unknown title",
            "thumbnail_url": self._extract_thumbnail_url(info),
            "filesize_bytes": size_bytes,
            "filesize_text": self._format_filesize(size_bytes),
            "duration_seconds": duration_seconds,
            "duration_text": self._format_duration(duration_seconds),
            "uploader": info.get("uploader") or info.get("channel") or "Unknown",
            "webpage_url": info.get("webpage_url") or "",
            "output_name": Path(str(output_name)).name,
            "subtitles": info.get("subtitles") or {},
            "ext": file_ext,
            "extractor": extractor_name,
        }

    def _build_download_item_text(self, record):
        title = record.get("title") or "Unknown title"
        size_text = record.get("filesize_text") or self._format_filesize(record.get("filesize_bytes"))
        duration_text = record.get("duration_text") or self._format_duration(record.get("duration_seconds"))
        uploader = record.get("uploader") or "Unknown"
        output_name = record.get("output_name") or "Unknown file"

        return (
            f"{title}\n"
            f"Size: {size_text} | Duration: {duration_text}\n"
            f"Uploader: {uploader}\n"
            f"Saved as: {output_name}"
        )
    
    def _create_download_item_allinfo(self, record):
        title = record.get("title") or "Unknown title"
        size_text = record.get("filesize_text") or self._format_filesize(record.get("filesize_bytes"))
        duration_text = record.get("duration_text") or self._format_duration(record.get("duration_seconds"))
        uploader = record.get("uploader") or "Unknown"
        webpage_url = record.get("webpage_url") or "No URL"
        output_name = record.get("output_name") or "Unknown file"
        extension = record.get("ext") or Path(str(output_name)).suffix.lstrip(".") or "Unknown"
        extractor = record.get("extractor") or "Unknown"

        resultdic = {
            "title": title, "size": size_text,
            "duration": duration_text,"uploader": uploader,
            "webpage_url": webpage_url,"output_name": output_name,
            "extension": extension,
            "extractor": extractor,
        }
        return "\n".join(f"{key}: {value}" for key, value in resultdic.items())


    def _add_download_record_to_list(self, record, insert_top=True):
        if not isinstance(record, dict):
            return

        list_item = QListWidgetItem(self._build_download_item_text(record))
        list_item.setData(Qt.ItemDataRole.UserRole, record)
        thumbnail_url = record.get("thumbnail_url")
        thumbnail_pixmap = self._fetch_thumbnail_pixmap(thumbnail_url)
        if not thumbnail_pixmap.isNull():
            if thumbnail_url:
                self.download_thumbnail_cache[str(thumbnail_url)] = thumbnail_pixmap
            icon_pixmap = self._scale_pixmap_to_cover_size(
                thumbnail_pixmap,
                self.download_history_list.iconSize(),
            )
            if not icon_pixmap.isNull():
                list_item.setIcon(QIcon(icon_pixmap))

        webpage_url = record.get("webpage_url")
        if webpage_url:
            list_item.setToolTip(str(webpage_url))

        if insert_top:
            self.download_history_list.insertItem(0, list_item)
        else:
            self.download_history_list.addItem(list_item)

    def _save_download_history_records(self):
        max_records = 250
        self.download_history_records = self.download_history_records[:max_records]

        history_path = self._download_history_path()
        with history_path.open("w", encoding="utf-8") as history_file:
            json.dump(self.download_history_records, history_file, ensure_ascii=True, indent=2)

    def _load_download_history_records(self):
        if not hasattr(self, "download_history_list"):
            return

        self.download_history_list.clear()
        self.download_history_records = []

        history_path = self._download_history_path()
        if not history_path.exists():
            return

        try:
            with history_path.open("r", encoding="utf-8") as history_file:
                loaded = json.load(history_file)
        except (OSError, json.JSONDecodeError):
            return

        if not isinstance(loaded, list):
            return

        for record in loaded:
            if not isinstance(record, dict):
                continue
            self.download_history_records.append(record)
            self._add_download_record_to_list(record, insert_top=False)

    def _normalize_download_items(self, info):
        if not isinstance(info, dict):
            return []

        if self._is_playlist_info(info):
            entries = self._extract_playlist_entries(info)
            return entries if entries else []

        return [info]

    def _append_download_history(self, info):
        if not hasattr(self, "download_history_list"):
            return

        downloaded_items = self._normalize_download_items(info)
        if not downloaded_items:
            return

        max_add = 80
        added_count = 0
        for downloaded_info in downloaded_items[:max_add]:
            record = self._serialize_download_item(downloaded_info)
            if not record:
                continue

            self.download_history_records.insert(0, record)
            self._add_download_record_to_list(record, insert_top=True)
            added_count += 1

        if added_count:
            self._save_download_history_records()

    def _set_download_thumbnail_placeholder(self, pixmap):
        if not hasattr(self, "download_thumbnail_placeholder"):
            return

        if pixmap and not pixmap.isNull():
            target_size = self.download_thumbnail_placeholder.size()
            cover = self._scale_pixmap_to_cover_size(pixmap, target_size)
            if not cover.isNull():
                self.download_thumbnail_placeholder.setPixmap(cover)
                self.download_thumbnail_placeholder.setText("")
                return

        self.download_thumbnail_placeholder.clear()
        self.download_thumbnail_placeholder.setText("Thumbnail unavailable")


    def _on_download_history_item_selected(self):
        if not hasattr(self, "download_history_list"):
            return

        current_item = self.download_history_list.currentItem()
        if not current_item:
            self._set_download_thumbnail_placeholder(QPixmap())
            return

        record = current_item.data(Qt.ItemDataRole.UserRole) #gets the data associated with the selected download history item, which should be a dict of the download info
        if not isinstance(record, dict):
            self._set_download_thumbnail_placeholder(QPixmap())
            return

        thumbnail_url = str(record.get("thumbnail_url") or "").strip()
        full_thumbnail = self.download_thumbnail_cache.get(thumbnail_url, QPixmap())
        if full_thumbnail.isNull() and thumbnail_url:
            full_thumbnail = self._fetch_thumbnail_pixmap(thumbnail_url)
            if not full_thumbnail.isNull():
                self.download_thumbnail_cache[thumbnail_url] = full_thumbnail

        if full_thumbnail.isNull():
            item_icon = current_item.icon()
            if not item_icon.isNull():
                full_thumbnail = item_icon.pixmap(self.download_thumbnail_placeholder.size())

        self._set_download_thumbnail_placeholder(full_thumbnail)
        self.download_info_placeholder.setText(self._create_download_item_allinfo(record))


    def _format_duration(self, seconds):
        if seconds in (None, ""):
            return "Unknown"

        try:
            total_seconds = int(seconds)
        except (TypeError, ValueError):
            return "Unknown"

        hours, remainder = divmod(total_seconds, 3600)
        minutes, secs = divmod(remainder, 60)
        if hours:
            return f"{hours}:{minutes:02d}:{secs:02d}"
        return f"{minutes}:{secs:02d}"

    def _format_filesize(self, size_bytes):
        if size_bytes in (None, ""):
            return "Unknown"

        try:
            size = float(size_bytes)
        except (TypeError, ValueError):
            return "Unknown"

        units = ["B", "KB", "MB", "GB", "TB"]
        unit_index = 0
        while size >= 1024 and unit_index < len(units) - 1:
            size /= 1024
            unit_index += 1

        if unit_index == 0:
            return f"{int(size)} {units[unit_index]}"
        return f"{size:.2f} {units[unit_index]}"

    def _normalize_preview_info(self, info):
        if not isinstance(info, dict):
            return {}

        # Playlist extractions return top-level playlist metadata; use first entry for video details.
        entries = info.get("entries")
        if entries:
            first_entry = next((entry for entry in entries if isinstance(entry, dict)), None)
            if first_entry:
                return first_entry

        return info

    def _reset_video_info_labels(self, exclude=None):
        exclude = exclude or set()
        for label_widget, prefix in self.video_info_label_prefixes.items():
            if label_widget in exclude:
                continue
            label_widget.setText(prefix)

    def _set_video_info_label_value(self, label_widget, value):
        prefix = self.video_info_label_prefixes.get(label_widget, "")
        safe_value = "Unknown" if value in (None, "") else str(value)
        label_widget.setText(f"{prefix} {safe_value}")

    def _set_loading_video_info_labels(self):
        self._set_video_info_label_value(self.ui.label, "Loading...")
        self._set_video_info_label_value(self.ui.label_10, "Loading...")
        self._set_video_info_label_value(self.ui.label_9, "Loading...")
        self._set_video_info_label_value(self.ui.label_8, "Loading...")

    def _set_video_info_status(self, status_text):
        self._set_video_info_label_value(self.ui.label, status_text)

    def _show_error_feedback(self, message):
        safe_text = str(message or "Unknown error")
        self._set_video_info_status(f"Error: {safe_text.splitlines()[0]}")
        self.ui.labelnew.setText(safe_text.splitlines()[0])
        QMessageBox.critical(self, "Cozydownloader", safe_text)

    def _set_video_info_labels_from_info(self, info):
        normalized = self._normalize_preview_info(info)

        title = normalized.get("title") or "Unknown"
        size_bytes = normalized.get("filesize") or normalized.get("filesize_approx")
        duration = self._format_duration(normalized.get("duration"))
        view_count = normalized.get("view_count")

        self._set_video_info_label_value(self.ui.label, title)
        self._set_video_info_label_value(self.ui.label_10, self._format_filesize(size_bytes))
        self._set_video_info_label_value(self.ui.label_9, duration)

        if view_count in (None, ""):
            formatted_views = "Unknown"
        else:
            try:
                formatted_views = f"{int(view_count):,}"
            except (TypeError, ValueError):
                formatted_views = str(view_count)
        self._set_video_info_label_value(self.ui.label_8, formatted_views)

    def _extract_thumbnail_url(self, info):
        if not isinstance(info, dict):
            return None

        thumbnail_url = info.get("thumbnail")
        if thumbnail_url:
            return thumbnail_url

        thumbnails = info.get("thumbnails")
        if isinstance(thumbnails, list) and thumbnails:
            last_thumbnail = thumbnails[-1]
            if isinstance(last_thumbnail, dict):
                return last_thumbnail.get("url")

        return None

    def _fetch_thumbnail_pixmap(self, thumbnail_url):
        if not thumbnail_url:
            return QPixmap()

        try:
            request = Request(thumbnail_url, headers={"User-Agent": "Mozilla/5.0"})
            with urlopen(request, timeout=12) as response:
                image_data = response.read()
            thumbnail_pixmap = QPixmap()
            if thumbnail_pixmap.loadFromData(image_data):
                return thumbnail_pixmap
        except Exception:
            return QPixmap()

        return QPixmap()

    def _populate_playlist_thumbnail_browser(self, info):
        self.playlist_thumbnail_list.clear()
        self.current_playlist_entries = []

        entries = self._extract_playlist_entries(info)
        if not self.pending_is_playlist or not entries:
            self.playlist_browser_widget.hide()
            return

        max_entries = 60
        self.current_playlist_entries = entries[:max_entries]

        for index, entry in enumerate(self.current_playlist_entries):
            title = entry.get("title") or f"Video {index + 1}"
            item = QListWidgetItem(title)
            item.setData(Qt.ItemDataRole.UserRole, index)
            item.setToolTip(title)

            thumbnail_url = self._extract_thumbnail_url(entry)
            pixmap = self._fetch_thumbnail_pixmap(thumbnail_url)
            if not pixmap.isNull():
                icon_pixmap = self._scale_pixmap_to_cover_size(pixmap, self.playlist_thumbnail_list.iconSize())
                item.setIcon(QIcon(icon_pixmap))

            self.playlist_thumbnail_list.addItem(item)

        self.playlist_browser_label.setText(
            f"Playlist videos ({len(entries)} found, showing {len(self.current_playlist_entries)})"
        )
        self.playlist_browser_widget.show()

        if self.playlist_thumbnail_list.count() > 0:
            self.playlist_thumbnail_list.setCurrentRow(0)

    def _on_playlist_thumbnail_selected(self):
        current_item = self.playlist_thumbnail_list.currentItem()
        if not current_item:
            return

        selected_index = current_item.data(Qt.ItemDataRole.UserRole)
        if not isinstance(selected_index, int):
            return

        if selected_index < 0 or selected_index >= len(self.current_playlist_entries):
            return

        selected_entry = self.current_playlist_entries[selected_index]
        self._set_preview_thumbnail_from_info(selected_entry)
        self._set_video_info_labels_from_info(selected_entry)

    def _extract_playlist_entries(self, info):
        if not isinstance(info, dict):
            return []

        raw_entries = info.get("entries")
        if not raw_entries:
            return []

        try:
            if isinstance(raw_entries, list):
                entries = raw_entries
            else:
                entries = list(raw_entries)
                info["entries"] = entries

            return [entry for entry in entries if isinstance(entry, dict)]
        except TypeError:
            return []

    def _is_playlist_info(self, info):
        if not isinstance(info, dict):
            return False

        info_type = str(info.get("_type", "")).lower()
        if info_type in {"playlist", "multi_video"}:
            return True

        return bool(self._extract_playlist_entries(info))

    def _update_playlist_detection_state(self, info):
        entries = self._extract_playlist_entries(info)
        self.pending_is_playlist = self._is_playlist_info(info)
        self._set_playlist_scope_controls_for_link_type(self.pending_is_playlist, len(entries))

    def _set_playlist_scope_controls_for_link_type(self, is_playlist, entry_count):
        if not hasattr(self, "playlist_scope_combo"):
            return

        self.playlist_scope_combo.blockSignals(True)
        self.playlist_scope_combo.setCurrentIndex(0)

        if is_playlist:
            item_word = "item" if entry_count == 1 else "items"
            count_text = f" ({entry_count} {item_word})" if entry_count else ""
            self.playlist_type_value.setText(f"Playlist{count_text}")
            self.playlist_scope_combo.setEnabled(True)
        else:
            self.playlist_type_value.setText("Single video")
            self.playlist_scope_combo.setEnabled(False)

        self.playlist_scope_combo.blockSignals(False)

    def _setup_settings_hover_gif(self):
        self.settings_button_default_icon = self.ui.Settings_BT.icon()
        self.settings_hover_movie = None
        self.settings_hover_playing_once = False
        self.settings_hover_seen_nonzero_frame = False

        gif_path = Path(__file__).resolve().parents[1] / "resource_files" / "settingsspin.gif"
        if not gif_path.exists():
            return

        movie = QMovie(str(gif_path))
        if not movie.isValid():
            return

        movie.frameChanged.connect(self._on_settings_hover_frame_changed)
        self.settings_hover_movie = movie
        self.ui.Settings_BT.installEventFilter(self)

    def _on_settings_hover_frame_changed(self, _frame_number):
        if not self.settings_hover_movie:
            return

        if self.settings_hover_playing_once:
            if _frame_number > 0:
                self.settings_hover_seen_nonzero_frame = True
            elif _frame_number == 0 and self.settings_hover_seen_nonzero_frame:
                self.settings_hover_movie.stop()
                self.settings_hover_playing_once = False
                self.settings_hover_seen_nonzero_frame = False
                self.ui.Settings_BT.setIcon(self.settings_button_default_icon)
                return

        current_frame = self.settings_hover_movie.currentPixmap()
        if current_frame.isNull():
            return

        target_size = self.ui.Settings_BT.iconSize()
        if target_size.isValid() and not target_size.isEmpty():
            current_frame = current_frame.scaled(
                target_size,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
            )

        self.ui.Settings_BT.setIcon(QIcon(current_frame))

    def eventFilter(self, watched, event):
        if watched is self.ui.Settings_BT and self.settings_hover_movie:
            if event.type() == QEvent.Type.Enter:
                self.settings_hover_movie.stop()
                self.settings_hover_playing_once = True
                self.settings_hover_seen_nonzero_frame = False
                self.settings_hover_movie.jumpToFrame(0)
                self.settings_hover_movie.start()
            elif event.type() == QEvent.Type.Leave:
                self.settings_hover_movie.stop()
                self.settings_hover_playing_once = False
                self.settings_hover_seen_nonzero_frame = False
                self.ui.Settings_BT.setIcon(self.settings_button_default_icon)

        if watched is getattr(self, "preview_download_bt", None):
            if event.type() == QEvent.Type.Enter:
                self.preview_download_leave_animation.stop()
                self.preview_download_enter_animation.setStartValue(self.preview_download_bt.minimumHeight())
                self.preview_download_enter_animation.start()
            elif event.type() == QEvent.Type.Leave:
                self.preview_download_enter_animation.stop()
                self.preview_download_leave_animation.setStartValue(self.preview_download_bt.minimumHeight())
                self.preview_download_leave_animation.start()

        return super().eventFilter(watched, event)

    def _setup_preview_download_hover_effect(self):
        base_height = max(self.preview_download_bt.sizeHint().height(), self.preview_download_bt.minimumHeight(), 34)
        self.preview_download_base_height = base_height
        self.preview_download_hover_height = base_height + 5

        self.preview_download_bt.setMinimumHeight(self.preview_download_base_height)

        self.preview_download_enter_animation = QPropertyAnimation(self.preview_download_bt, b"minimumHeight")
        self.preview_download_enter_animation.setDuration(130)
        self.preview_download_enter_animation.setEndValue(self.preview_download_hover_height)
        self.preview_download_enter_animation.setEasingCurve(QEasingCurve.OutCubic)

        self.preview_download_leave_animation = QPropertyAnimation(self.preview_download_bt, b"minimumHeight")
        self.preview_download_leave_animation.setDuration(130)
        self.preview_download_leave_animation.setEndValue(self.preview_download_base_height)
        self.preview_download_leave_animation.setEasingCurve(QEasingCurve.OutCubic)

        self.preview_download_bt.installEventFilter(self)

    def _setup_download_button_feedback(self):
        self.preview_download_default_text = self.preview_download_bt.text()
        self.preview_download_default_icon = self.preview_download_bt.icon()
        self.preview_download_loading_movie = None

        gif_path = Path(__file__).resolve().parents[1] / "resource_files" / "downloading.gif"
        if not gif_path.exists():
            return

        movie = QMovie(str(gif_path))
        if not movie.isValid():
            return

        movie.frameChanged.connect(self._on_preview_download_loading_frame_changed)
        self.preview_download_loading_movie = movie

    def _on_preview_download_loading_frame_changed(self, _frame_number):
        if not self.preview_download_loading_movie:
            return

        pixmap = self.preview_download_loading_movie.currentPixmap()
        if pixmap.isNull():
            return

        target_size = QSize(60, 60)
        scaled = pixmap.scaled(
            target_size,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )
        self.preview_download_bt.setIcon(QIcon(scaled))
        self.preview_download_bt.setIconSize(target_size)

    def _set_download_button_busy(self, is_busy):
        if is_busy:
            self.preview_download_bt.setText("Downloading...")
            if self.preview_download_loading_movie:
                self.preview_download_loading_movie.stop()
                self.preview_download_loading_movie.start()
        else:
            if self.preview_download_loading_movie:
                self.preview_download_loading_movie.stop()
            self.preview_download_bt.setIcon(self.preview_download_default_icon)
            self.preview_download_bt.setText(self.preview_download_default_text)

    def _set_preview_thumbnail_from_info(self, info):
        thumbnail_url = None

        if isinstance(info, dict):
            thumbnail_url = info.get("thumbnail")

            if not thumbnail_url:
                thumbnails = info.get("thumbnails")
                if isinstance(thumbnails, list) and thumbnails:
                    thumbnail_url = thumbnails[-1].get("url")

            if not thumbnail_url:
                entries = info.get("entries")
                if entries:
                    first_entry = next((entry for entry in entries if isinstance(entry, dict)), None)
                    if first_entry:
                        thumbnail_url = first_entry.get("thumbnail")
                        if not thumbnail_url:
                            entry_thumbnails = first_entry.get("thumbnails")
                            if isinstance(entry_thumbnails, list) and entry_thumbnails:
                                thumbnail_url = entry_thumbnails[-1].get("url")

        if not thumbnail_url:
            self.current_preview_thumbnail_pixmap = None
            self.ui.imagePlaceholder_lb.setText("Thumbnail unavailable")
            self.ui.imagePlaceholder_lb.setPixmap(QPixmap())
            return

        try:
            request = Request(thumbnail_url, headers={"User-Agent": "Mozilla/5.0"})
            with urlopen(request, timeout=15) as response:
                image_data = response.read()

            thumbnail_pixmap = QPixmap()
            if not thumbnail_pixmap.loadFromData(image_data):
                self.current_preview_thumbnail_pixmap = None
                self.ui.imagePlaceholder_lb.setText("Thumbnail failed to load")
                self.ui.imagePlaceholder_lb.setPixmap(QPixmap())
                return

            self.current_preview_thumbnail_pixmap = thumbnail_pixmap
            self._refresh_preview_thumbnail_display()
            self.ui.imagePlaceholder_lb.setText("")
        except Exception:
            self.current_preview_thumbnail_pixmap = None
            self.ui.imagePlaceholder_lb.setText("Thumbnail failed to load")
            self.ui.imagePlaceholder_lb.setPixmap(QPixmap())


    def update_checkurl_visibility(self, text):
        self.ui.CheckURL_bt.setVisible(bool(text.strip()))

    def sync_user_input_preview(self, text):
        self.ui.userInput_le.setText(text)

    def go_home_page(self):
        self.loading_movie.stop()
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageHome)

    def go_page_three(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageEmpty)
        if self.loading_movie.isValid() and self.loading_movie.state() != QMovie.Running:
            self.loading_movie.start()

    def go_downloadspage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_downloads)

    def go_settings_window(self):
        if self.settings_window is None:
            self.settings_window = settingsWindow(self.apply_home_background)
            self.settings_window.sleep_time_changed.connect(self._on_sleep_time_changed)
            self.settings_window.cookies_enabled_changed.connect(self._on_cookies_enabled_changed)
            self.settings_window.gui_mode_changed.connect(self._on_gui_mode_changed)
        self.settings_window.show()

    def _on_sleep_time_changed(self, sleep_seconds):
        try:
            self.sleep_time_seconds = max(0, int(sleep_seconds))
        except (TypeError, ValueError):
            self.sleep_time_seconds = 0

    def _on_cookies_enabled_changed(self, enabled):
        self.has_cookies = bool(enabled)

    def _on_gui_mode_changed(self, is_light_mode_enabled):
        """Handle GUI mode change and apply theme to main window."""
        self.is_light_mode_enabled = bool(is_light_mode_enabled)
        self._apply_theme()
        self._apply_saved_home_background()

    def _clear_home_background(self):
        for previous_movie in self.page_background_movies.values():
            previous_movie.stop()
        self.page_background_movies = {}

        for background_label in self.page_background_labels.values():
            background_label.clear()
            background_label.hide()

    def _apply_saved_home_background(self):
        saved_background = self._load_saved_home_background_path(self.is_light_mode_enabled)
        self._clear_home_background()
        if saved_background:
            self.apply_home_background(saved_background)

    def _detect_cookies_browser(self):
        local_app_data = os.getenv("LOCALAPPDATA", "")
        roaming_app_data = os.getenv("APPDATA", "")

        browser_paths = []
        if local_app_data:
            browser_paths.extend([
                ("chrome", Path(local_app_data) / "Google" / "Chrome" / "User Data"),
                ("edge", Path(local_app_data) / "Microsoft" / "Edge" / "User Data"),
                ("brave", Path(local_app_data) / "BraveSoftware" / "Brave-Browser" / "User Data"),
                ("opera", Path(local_app_data) / "Opera Software" / "Opera Stable"),
            ])
        if roaming_app_data:
            browser_paths.append(("firefox", Path(roaming_app_data) / "Mozilla" / "Firefox" / "Profiles"))

        for browser_name, browser_profile_path in browser_paths:
            if browser_profile_path.exists():
                return browser_name
        return None


    def open_ytdlp_github(self): #opens the ytdlp github page <3
        QDesktopServices.openUrl(QUrl("https://github.com/yt-dlp/yt-dlp"))

    def open_our_github(self):
        QDesktopServices.openUrl(QUrl("https://github.com/cozidesire/cozydownloader"))

    def _add_hover_scaling(self, button, default_size, hover_size, duration=200): #hover scaling for buttons
        """Add hover scaling effect to a button by storing size info and overriding mouse events."""
        button.default_icon_size = default_size
        button.hover_icon_size = hover_size
        
        # Create animations
        button.enter_animation = QPropertyAnimation(button, b"iconSize")
        button.enter_animation.setDuration(duration)  # milliseconds
        button.enter_animation.setEndValue(hover_size)  # Direct QSize
        button.enter_animation.setEasingCurve(QEasingCurve.OutCubic)  # Smooth easing
        
        button.leave_animation = QPropertyAnimation(button, b"iconSize")
        button.leave_animation.setDuration(duration)
        button.leave_animation.setEndValue(default_size)  # Direct QSize
        button.leave_animation.setEasingCurve(QEasingCurve.OutCubic)
        
        # Store original enterEvent and leaveEvent
        original_enter = button.enterEvent
        original_leave = button.leaveEvent
        
        def smooth_enter_event(event):
            button.leave_animation.stop()
            button.enter_animation.start()
            if original_enter:
                original_enter(event)

        def smooth_leave_event(event):
            button.enter_animation.stop()
            button.leave_animation.start()
            if original_leave:
                original_leave(event)
        
        button.enterEvent = smooth_enter_event
        button.leaveEvent = smooth_leave_event

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._resize_page_background_labels()
        self._refresh_preview_thumbnail_display()

    def _scale_pixmap_to_cover_size(self, pixmap, target_size):
        if pixmap.isNull() or not target_size.isValid() or target_size.isEmpty():
            return QPixmap()

        scaled = pixmap.scaled(
            target_size,
            Qt.AspectRatioMode.KeepAspectRatioByExpanding,
            Qt.TransformationMode.SmoothTransformation,
        )

        if scaled.isNull():
            return QPixmap()

        x_offset = max(0, (scaled.width() - target_size.width()) // 2)
        y_offset = max(0, (scaled.height() - target_size.height()) // 2)
        return scaled.copy(x_offset, y_offset, target_size.width(), target_size.height())

    def _refresh_preview_thumbnail_display(self):
        if not self.current_preview_thumbnail_pixmap or self.current_preview_thumbnail_pixmap.isNull():
            return

        target_size = self.ui.imagePlaceholder_lb.size()
        cover = self._scale_pixmap_to_cover_size(self.current_preview_thumbnail_pixmap, target_size)
        if cover.isNull():
            return

        self.ui.imagePlaceholder_lb.setScaledContents(False)
        self.ui.imagePlaceholder_lb.setPixmap(cover)

    def _on_stacked_page_changed(self, _index):
        # Page geometry can change on navigation; resync background immediately.
        QTimer.singleShot(0, self._resize_page_background_labels)

    def _resize_page_background_labels(self):
        for page, background_label in self.page_background_labels.items():
            background_label.setGeometry(0, 0, page.width(), page.height())
            page_movie = self.page_background_movies.get(page)
            if page_movie and page_movie.isValid():
                page_movie.setScaledSize(background_label.size())

    def _background_config_path(self):
        config_dir = self._config_dir()
        config_dir.mkdir(parents=True, exist_ok=True)
        return config_dir / "background_settings.json"

    def _project_base_dir(self):
        if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
            return Path(sys._MEIPASS)
        return Path(__file__).resolve().parents[1]

    def _assets_dir(self):
        return self._project_base_dir() / "assets"

    def _config_dir(self):
        return _effective_config_dir()

    def _bundled_background_config_path(self):
        return self._project_base_dir() / "config" / "background_settings.json"

    def _load_background_config_data(self):
        for config_path in (self._background_config_path(), self._bundled_background_config_path()):
            if not config_path.exists():
                continue

            try:
                with config_path.open("r", encoding="utf-8") as config_file:
                    config_data = json.load(config_file)
                if isinstance(config_data, dict):
                    return config_data
            except (json.JSONDecodeError, OSError, AttributeError, TypeError):
                continue

        return {}

    def _resolve_media_path(self, stored_path):
        if not stored_path:
            return None

        raw_path = Path(str(stored_path))
        if raw_path.is_absolute() and raw_path.exists():
            return raw_path

        normalized_relative = Path(str(stored_path).replace("\\", "/"))
        candidate = self._project_base_dir() / normalized_relative
        if candidate.exists():
            return candidate

        fallback_asset = self._assets_dir() / raw_path.name
        if fallback_asset.exists():
            return fallback_asset

        return None

    def _load_saved_home_background_path(self, is_light_mode_enabled=None):
        if is_light_mode_enabled is None:
            is_light_mode_enabled = self.is_light_mode_enabled

        default_background = self.default_background_by_mode.get(
            bool(is_light_mode_enabled),
            Path("assets/StarfieldSimulation004.gif"),
        )
        config_data = self._load_background_config_data()
        if not config_data:
            return default_background.as_posix()

        mode_key = "home_background_path_light" if bool(is_light_mode_enabled) else "home_background_path_dark"
        stored_path = str(config_data.get(mode_key, "")).strip()
        if not stored_path:
            # Backward compatibility with pre-theme settings payloads.
            stored_path = str(config_data.get("home_background_path", "")).strip()
        return stored_path or default_background.as_posix()

    def _load_saved_sleep_time(self):
        config_data = self._load_background_config_data()
        raw_value = config_data.get("default_sleep_seconds", 0)
        try:
            return max(0, int(raw_value))
        except (TypeError, ValueError):
            return 0
        
    def _load_saved_cookies_enabled(self):
        config_data = self._load_background_config_data()
        raw_value = config_data.get("cookies_enabled", False)
        return bool(raw_value)

    def _load_saved_theme(self):
        """Load the saved theme mode. Dark mode is the default."""
        config_data = self._load_background_config_data()
        raw_value = config_data.get("gui_mode_enabled", False)
        return bool(raw_value)  # Returns True for light mode, False for dark mode

    def _apply_theme(self):
        """Apply the current theme mode to the main window."""
        # is_light_mode_enabled is True for light mode, False for dark mode
        # get_mainwindow_stylesheet expects True for dark mode, False for light mode
        is_dark_mode = not self.is_light_mode_enabled
        stylesheet = get_mainwindow_stylesheet(is_dark_mode)
        self.setStyleSheet(stylesheet)


    def apply_home_background(self, file_path):
        selected_path = self._resolve_media_path(file_path)
        if not selected_path:
            self._clear_home_background()
            return

        # Clear previous media before applying a new background.
        self._clear_home_background()

        for background_label in self.page_background_labels.values():
            background_label.show()

        if selected_path.suffix.lower() == ".gif":
            for page, background_label in self.page_background_labels.items():
                page_movie = QMovie(str(selected_path))
                background_label.setMovie(page_movie)
                if page_movie.isValid():
                    page_movie.setScaledSize(background_label.size())
                    page_movie.start()
                    self.page_background_movies[page] = page_movie
                else:
                    background_label.hide()
        else:
            pixmap = QPixmap(str(selected_path))
            if pixmap.isNull():
                for background_label in self.page_background_labels.values():
                    background_label.hide()
                return
            for background_label in self.page_background_labels.values():
                background_label.setPixmap(pixmap)

        for background_label in self.page_background_labels.values():
            background_label.lower()
        self._resize_page_background_labels()
    