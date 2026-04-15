"""
Theme management system for light/dark mode support.
"""

# Dark mode stylesheet for main window
DARK_MODE_MAINWINDOW = u"""
#VideoInfoWid{
	background-color: rgba(0, 0, 0,0.6);
	border-radius:16px;
	border: none;
}

#optionslayout{
	background-color: rgba(77, 77, 77,0.4);
	border-radius:16px;
	border: none;
}

#Downloads_info{
	background-color: rgba(77, 77, 77,0.4);
}

#label1{ 
	color: white;
	font-size: 38px;
	text-align: center;
	border-radius: 14px;
	border: none;
}

#gridLayout_2{
    background-color: rgba(0, 0, 0, 0);
    border-radius: 12px;
}

#Biglabel_DWL{
	background-color: rgba(0, 0, 0,0.7);
}

#imagePlaceholder_lb{
	background-color: none;
	border: 1px solid rgba(238, 238, 238,0.7);
	border-radius: 14px;
}

#playlistThumbs_lw{
	background-color: transparent;
	border: 1px solid rgba(255, 255, 255,0.3);
}

#downloadHistory_lw{
	background-color: transparent;
	border: 1px solid rgba(255, 255, 255,0.4)
}


#URL_placement{
	border-radius: 10px;
	padding: 6px;
    min-height: 20px;
	background-color: rgba(59, 59, 59,0.7);
	border: 1px solid rgba(249, 249, 249,0.3);
	color: white;
}

#kuddos_bt{
	background-color: transparent;
	border: none;
}

#kuddos_bt:hover{
	background-color: transparent;
}

#centralwidget {
    background-color: black;
}

#Settings_BT{
	background-color: transparent;
	border: none;
}

#Downloads_BT{
	background-color: transparent;
	border: none;
}

#goPage3_bt{
	border-radius: 14px;
	background-color: transparent;
	border: none;
}

#goPage3_bt:hover {
	border-radius: 14px;
	background-color: transparent;
}

#BackHome_Downloads{
	background-color: transparent;
	border:none;
	border-radius: 5px;
}

#home_kudopage_bt{
	background-color: transparent;
	border:none;
	border-radius: 5px;
}

#backHome_bt{
	background-color: transparent;
	border:none;
	border-radius: 5px;
}

#backHome_bt:hover{
	background-color: rgba(255, 255, 255, 0.1);
	border: 1px solid white;
}

#CheckURL_bt{
    background-color: rgba(0, 0, 0,0.7);
    color: white;
    font-size: 15px;
	text-align: center;
	border: 1px solid rgba(185, 185, 185,0.5);
	border-radius: 7px;
	padding: 4px;
}

#CheckURL_bt:hover{
    background-color: rgba(100, 100, 100, 0.5);
    border: 1px solid #888;
}

#CheckURL_bt:pressed{
    background-color: rgba(150, 150, 150, 0.5);
}

#previewDownload_bt{
	background-color: rgba(26, 26, 26,0.7);
	border: 1px solid rgba(255, 255, 255,0.3);
}

#previewDownload_bt:hover{
	background-color: rgba(26, 26, 26,0.8);
	border: 1px solid rgba(255, 255, 255,0.6);
}

QPushButton {
    background-color: rgba(0, 0, 0,0.8);
    color: white;
    font-size: 15px;
	text-align: center;
	border: 1px solid white;
	border-radius: 7px;
	padding: 4px;
}

QPushButton:hover{
    background-color: rgba(100, 100, 100, 0.5);
    border: 1px solid #888;
}

QPushButton:pressed{
    background-color: rgba(150, 150, 150, 0.5);
}

QLabel {
	color: white;
}

QComboBox {
	background-color: rgba(59, 59, 59, 0.7);
	color: white;
	border: 1px solid rgba(185, 185, 185, 0.5);
	border-radius: 5px;
	padding: 4px;
}

QComboBox::drop-down {
	border: none;
}

QComboBox QAbstractItemView {
	background-color: rgba(59, 59, 59, 0.9);
	color: white;
	selection-background-color: rgba(100, 100, 100, 0.8);
}

QLineEdit {
	background-color: rgba(59, 59, 59, 0.7);
	color: white;
	border: 1px solid rgba(185, 185, 185, 0.5);
	border-radius: 5px;
	padding: 4px;
}

QSpinBox {
	background-color: rgba(59, 59, 59, 0.7);
	color: white;
	border: 1px solid rgba(185, 185, 185, 0.5);
	border-radius: 5px;
	padding: 4px;
}

QListWidget {
	background-color: rgba(59, 59, 59, 0.5);
	color: white;
	border: 1px solid rgba(185, 185, 185, 0.3);
}

QListWidget::item {
	border: 1px solid transparent;
	padding: 4px;
}

QListWidget::item:selected {
	background-color: rgba(100, 100, 100, 0.7);
	border: 1px solid rgba(100, 100, 100, 0.7);
}
"""

# Light mode stylesheet for main window
LIGHT_MODE_MAINWINDOW = u"""
#VideoInfoWid{
	background-color: rgba(255, 255, 255, 0.85);
	border-radius:16px;
	border: 1px solid rgba(200, 200, 200, 0.5);
}

#optionslayout{
	background-color: rgba(240, 240, 240, 0.7);
	border-radius:16px;
	border: 1px solid rgba(200, 200, 200, 0.4);
}

#Downloads_info{
	background-color: rgba(240, 240, 240, 0.7);
}

#label1{ 
	color: black;
	font-size: 38px;
	text-align: center;
	border-radius: 14px;
	border: none;
}

#gridLayout_2{
    background-color: rgba(255, 255, 255, 0);
    border-radius: 12px;
}


#Biglabel_DWL{
	background-color: rgba(255, 255, 255, 0.9);
}

#imagePlaceholder_lb{
	background-color: white;
	border: 1px solid rgba(150, 150, 150, 0.5);
	border-radius: 14px;
}

#playlistThumbs_lw{
	background-color: white;
	border: 1px solid rgba(150, 150, 150, 0.5);
}

#downloadHistory_lw{
	background-color: white;
	border: 1px solid rgba(150, 150, 150, 0.5);
}

#URL_placement{
	border-radius: 10px;
	padding: 6px;
    min-height: 20px;
	background-color: rgba(240, 240, 240, 0.9);
	border: 1px solid rgba(100, 100, 100, 0.3);
	color: black;
}

#kuddos_bt{
	background-color: transparent;
	border: none;
}

#kuddos_bt:hover{
	background-color: transparent;
}

#centralwidget {
    background-color: white;
}

#Settings_BT{
	background-color: transparent;
	border: none;
}

#Downloads_BT{
	background-color: transparent;
	border: none;
}

#goPage3_bt{
	border-radius: 14px;
	background-color: transparent;
	border: none;
}

#goPage3_bt:hover {
	border-radius: 14px;
	background-color: transparent;
}

#BackHome_Downloads{
	background-color: transparent;
	border:none;
	border-radius: 5px;
}

#home_kudopage_bt{
	background-color: transparent;
	border:none;
	border-radius: 5px;
}

#backHome_bt{
	background-color: transparent;
	border:none;
	border-radius: 5px;
}

#backHome_bt:hover{
	background-color: rgba(0, 0, 0, 0.05);
	border: 1px solid #333;
}

#CheckURL_bt{
    background-color: rgba(230, 230, 230, 0.9);
    color: black;
    font-size: 15px;
	text-align: center;
	border: 1px solid rgba(100, 100, 100, 0.4);
	border-radius: 7px;
	padding: 4px;
}

#CheckURL_bt:hover{
    background-color: rgba(200, 200, 200, 0.7);
    border: 1px solid #666;
}

#CheckURL_bt:pressed{
    background-color: rgba(180, 180, 180, 0.8);
}

#previewDownload_bt{
	background-color: rgba(230, 230, 230, 0.8);
	border: 1px solid rgba(100, 100, 100, 0.4);
}

#previewDownload_bt:hover{
	background-color: rgba(200, 200, 200, 0.8);
	border: 1px solid rgba(100, 100, 100, 0.6);
}

QPushButton {
    background-color: rgba(220, 220, 220, 0.9);
    color: black;
    font-size: 15px;
	text-align: center;
	border: 1px solid #666;
	border-radius: 7px;
	padding: 4px;
}

QPushButton:hover{
    background-color: rgba(200, 200, 200, 0.8);
    border: 1px solid #444;
}

QPushButton:pressed{
    background-color: rgba(180, 180, 180, 0.8);
}

QLabel {
	color: black;
}

QComboBox {
	background-color: rgba(240, 240, 240, 0.9);
	color: black;
	border: 1px solid rgba(100, 100, 100, 0.4);
	border-radius: 5px;
	padding: 4px;
}

QComboBox::drop-down {
	border: none;
}

QComboBox QAbstractItemView {
	background-color: rgba(250, 250, 250, 0.95);
	color: black;
	selection-background-color: rgba(200, 200, 200, 0.6);
}

QLineEdit {
	background-color: rgba(240, 240, 240, 0.9);
	color: black;
	border: 1px solid rgba(100, 100, 100, 0.4);
	border-radius: 5px;
	padding: 4px;
}

QSpinBox {
	background-color: rgba(240, 240, 240, 0.9);
	color: black;
	border: 1px solid rgba(100, 100, 100, 0.4);
	border-radius: 5px;
	padding: 4px;
}

QListWidget {
	background-color: rgba(250, 250, 250, 0.8);
	color: black;
	border: 1px solid rgba(100, 100, 100, 0.3);
}

QListWidget::item {
	border: 1px solid transparent;
	padding: 4px;
}

QListWidget::item:selected {
	background-color: rgba(200, 200, 200, 0.5);
	border: 1px solid rgba(200, 200, 200, 0.5);
}

/* Keep the secret/empty page unchanged while light mode is enabled. */
#pageEmpty {
	background-color: black;
}

#pageEmpty QLabel {
	color: white;
}

#pageEmpty QPushButton {
	background-color: transparent;
	color: white;
	border: none;
}

#pageEmpty QPushButton:hover {
	background-color: rgba(255, 255, 255, 0.1);
	border: 1px solid white;
}

#pageEmpty QPushButton:pressed {
	background-color: rgba(150, 150, 150, 0.5);
}
"""

# Dark mode stylesheet for settings window
DARK_MODE_SETTINGS = u"""
#MainWindow{
  background-color: rgb(24, 24, 24)
}

#sleeptime__int{
  border: 1px solid rgba(255, 255, 255,0.7);
  border-radius: 3px;
  background-color: rgba(59, 59, 59, 0.7);
  color: white;
  padding: 4px;
}

#controls{
  background-color: rgba(0, 0, 0,0.5);
  border: none;
  border-radius: 12px;
}

QLabel {
  color: white;
}

QToolButton {
  background-color: transparent;
  border: none;
}

QPushButton {
  background-color: rgba(0, 0, 0, 0.8);
  color: white;
  border: 1px solid white;
  border-radius: 7px;
  padding: 4px;
  font-size: 15px;
}

QPushButton:hover {
  background-color: rgba(100, 100, 100, 0.5);
  border: 1px solid #888;
}

QPushButton:pressed {
  background-color: rgba(150, 150, 150, 0.5);
}
"""

# Light mode stylesheet for settings window
LIGHT_MODE_SETTINGS = u"""
#MainWindow{
  background-color: rgb(245, 245, 245)
}

#sleeptime__int{
  border: 1px solid rgba(100, 100, 100, 0.4);
  border-radius: 3px;
  background-color: rgba(240, 240, 240, 0.9);
  color: black;
  padding: 4px;
}

#controls{
  background-color: rgba(255, 255, 255, 0.8);
  border: 1px solid rgba(100, 100, 100, 0.3);
  border-radius: 12px;
}

QToolButton {
  background-color: transparent;
  border: none;
}

QLabel {
  color: black;
}

QPushButton {
  background-color: rgba(220, 220, 220, 0.9);
  color: black;
  border: 1px solid #666;
  border-radius: 7px;
  padding: 4px;
  font-size: 15px;
}

QPushButton:hover {
  background-color: rgba(200, 200, 200, 0.8);
  border: 1px solid #444;
}

QPushButton:pressed {
  background-color: rgba(180, 180, 180, 0.8);
}
"""


def get_mainwindow_stylesheet(is_dark_mode: bool) -> str:
    """Get the stylesheet for the main window based on the theme mode."""
    return DARK_MODE_MAINWINDOW if is_dark_mode else LIGHT_MODE_MAINWINDOW


def get_settings_stylesheet(is_dark_mode: bool) -> str:
    """Get the stylesheet for the settings window based on the theme mode."""
    return DARK_MODE_SETTINGS if is_dark_mode else LIGHT_MODE_SETTINGS
