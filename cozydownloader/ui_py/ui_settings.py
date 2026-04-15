# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settingsWin.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect, QPropertyAnimation, QEasingCurve, Property,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter, QPen,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QToolButton, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(373, 411)
        MainWindow.setStyleSheet(u"#MainWindow{\n"
"  background-color: rgb(24, 24, 24)\n"
"\n"
"}\n"
"\n"
"#sleeptime__int{\n"
"  border: 1px solid rgba(255, 255, 255,0.7);\n"
"  border-radius: 3px;\n"
"	\n"
"}\n"
"\n"
"QToolButton{\n"
"\n"
"	background-color: transparent;\n"
"	border: none;\n"
"}\n"
"\n"
"\n"
"#controls{\n"
"  background-color: rgba(0, 0, 0,0.5);\n"
"  border: none;\n"
"  border-radius: 12px;\n"
"\n"
"}\n"
"\n"
"QCheckBox#pushButton::indicator,\n"
"QCheckBox#pushButton_2::indicator{\n"
"  width: 50px;\n"
"  height: 26px;\n"
"  border-radius: 13px;\n"
"  border: 1px solid rgba(255,255,255,0.75);\n"
"  background-color: rgba(120,120,120,0.45);\n"
"}\n"
"\n"
"QCheckBox#pushButton::indicator:checked,\n"
"QCheckBox#pushButton_2::indicator:checked{\n"
"  background-color: rgba(255, 255, 255,0.8);\n"
"  border: 1px solid rgba(255,255,255,0.95);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.SettingslabelTittle = QLabel(self.centralwidget)
        self.SettingslabelTittle.setObjectName(u"SettingslabelTittle")
        font = QFont()
        font.setBold(True)
        font.setItalic(True)
        self.SettingslabelTittle.setFont(font)

        self.verticalLayout.addWidget(self.SettingslabelTittle)

        self.controls = QWidget(self.centralwidget)
        self.controls.setObjectName(u"controls")
        self.gridLayout = QGridLayout(self.controls)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(8)
        self.pushButton = QCheckBox(self.controls)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton, 0, 2, 1, 1)

        self.pushButton_2 = QCheckBox(self.controls)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_2, 1, 2, 1, 1)

        self.toolButton = QToolButton(self.controls)
        self.toolButton.setObjectName(u"toolButton")
        icon = QIcon()
        icon.addFile(u":/icons/moon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QSize(32, 30))

        self.gridLayout.addWidget(self.toolButton, 1, 1, 1, 1)

        self.CookiesLabel = QLabel(self.controls)
        self.CookiesLabel.setObjectName(u"CookiesLabel")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        self.CookiesLabel.setFont(font1)
        self.CookiesLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.CookiesLabel, 0, 0, 1, 1)

        self.GUImodeLabel = QLabel(self.controls)
        self.GUImodeLabel.setObjectName(u"GUImodeLabel")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setItalic(False)
        self.GUImodeLabel.setFont(font2)
        self.GUImodeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.GUImodeLabel, 1, 0, 1, 1)

        self.DefaulSleepLabel = QLabel(self.controls)
        self.DefaulSleepLabel.setObjectName(u"DefaulSleepLabel")
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(True)
        self.DefaulSleepLabel.setFont(font3)
        self.DefaulSleepLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.DefaulSleepLabel, 2, 0, 1, 1)

        self.toolButton_2 = QToolButton(self.controls)
        self.toolButton_2.setObjectName(u"toolButton_2")
        icon1 = QIcon()
        icon1.addFile(u":/icons/sun.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton_2.setIcon(icon1)
        self.toolButton_2.setIconSize(QSize(30, 28))

        self.gridLayout.addWidget(self.toolButton_2, 1, 3, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.verticalSpacer_2, 3, 0, 1, 3)

        self.sleeptime__int = QSpinBox(self.controls)
        self.sleeptime__int.setObjectName(u"sleeptime__int")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sleeptime__int.sizePolicy().hasHeightForWidth())
        self.sleeptime__int.setSizePolicy(sizePolicy1)
        self.sleeptime__int.setMinimumSize(QSize(34, 0))
        self.sleeptime__int.setMaximum(3600)

        self.gridLayout.addWidget(self.sleeptime__int, 2, 1, 1, 2)

        self.Upload_bt = QPushButton(self.controls)
        self.Upload_bt.setObjectName(u"Upload_bt")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Upload_bt.sizePolicy().hasHeightForWidth())
        self.Upload_bt.setSizePolicy(sizePolicy2)
        self.Upload_bt.setMinimumSize(QSize(0, 40))
        self.Upload_bt.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.Upload_bt, 5, 0, 1, 4)

        self.BackgroundLabel = QLabel(self.controls)
        self.BackgroundLabel.setObjectName(u"BackgroundLabel")
        sizePolicy1.setHeightForWidth(self.BackgroundLabel.sizePolicy().hasHeightForWidth())
        self.BackgroundLabel.setSizePolicy(sizePolicy1)
        self.BackgroundLabel.setMinimumSize(QSize(0, 25))
        self.BackgroundLabel.setFont(font3)
        self.BackgroundLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.BackgroundLabel, 4, 0, 1, 4)


        self.verticalLayout.addWidget(self.controls)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.SettingslabelTittle.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.CookiesLabel.setText(QCoreApplication.translate("MainWindow", u"Cookies", None))
        self.GUImodeLabel.setText(QCoreApplication.translate("MainWindow", u"GUI mode", None))
        self.DefaulSleepLabel.setText(QCoreApplication.translate("MainWindow", u"Default sleep time", None))
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.Upload_bt.setText(QCoreApplication.translate("MainWindow", u"Upload file", None))
        self.BackgroundLabel.setText(QCoreApplication.translate("MainWindow", u"Change background", None))
    # retranslateUi

class AnimatedToggle(QWidget):
    """A custom toggle widget with an animated knob."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(52, 28)
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        self._checked = False
        self._slider_pos = 0

        self.animation = QPropertyAnimation(self, b"slider_pos")
        self.animation.setDuration(180)
        self.animation.setEasingCurve(QEasingCurve.Type.InOutCubic)

    @Property(int)
    def slider_pos(self):
        return self._slider_pos

    @slider_pos.setter
    def slider_pos(self, value):
        self._slider_pos = int(value)
        self.update()

    def isChecked(self):
        return self._checked

    def setChecked(self, checked):
        checked = bool(checked)
        if self._checked == checked and self.animation.state() != QPropertyAnimation.State.Running:
            self._slider_pos = 24 if checked else 0
            self.update()
            return

        self._checked = checked
        self.animation.stop()
        self.animation.setStartValue(self._slider_pos)
        self.animation.setEndValue(24 if checked else 0)
        self.animation.start()

    def toggle(self):
        self.setChecked(not self._checked)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.toggle()
        super().mousePressEvent(event)

    def paintEvent(self, event):
        _ = event
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        width = self.width()
        height = self.height()
        knob_radius = 10

        if self._checked:
            track_color = QColor(52, 132, 255)
            border_color = QColor(122, 178, 255)
        else:
            track_color = QColor(120, 120, 120)
            border_color = QColor(255, 255, 255, 190)

        painter.setBrush(track_color)
        painter.setPen(QPen(border_color, 2))
        painter.drawRoundedRect(0, 0, width, height, height / 2, height / 2)

        painter.setBrush(QColor(255, 255, 255))
        painter.setPen(Qt.PenStyle.NoPen)
        knob_x = 4 + self._slider_pos
        knob_y = (height - knob_radius * 2) // 2
        painter.drawEllipse(knob_x, knob_y, knob_radius * 2, knob_radius * 2)
