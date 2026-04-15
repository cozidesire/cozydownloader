# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1103, 649)
        icon = QIcon()
        icon.addFile(u":/icons/meow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"#VideoInfoWid{\n"
"	background-color: rgba(0, 0, 0,0.6);\n"
"	border-radius:16px;\n"
"	border: none;\n"
"}\n"
"\n"
"#optionslayout{\n"
"	background-color: rgba(77, 77, 77,0.4);\n"
"	border-radius:16px;\n"
"	border: none;\n"
"}\n"
"\n"
"#Downloads_info{\n"
"	background-color: rgba(77, 77, 77,0.4);\n"
"\n"
"}\n"
"\n"
"#label1{ \n"
"	color: white;\n"
"	font-size: 38px;\n"
"	text-align: center;\n"
"	border-radius: 14px;\n"
"	border: none;\n"
"}\n"
"\n"
"\n"
"#gridLayout_2{\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    border-radius: 12px;\n"
"}\n"
"\n"
"#Biglabel_DWL{\n"
"	background-color: rgba(0, 0, 0,0.7);\n"
"\n"
"}\n"
"\n"
"#imagePlaceholder_lb{\n"
"	background-color: none;\n"
"	border: 1px solid rgba(238, 238, 238,0.7);\n"
"}\n"
"\n"
"#playlistThumbs_lw{\n"
"	background-color: transparent;\n"
"	border: 1px solid rgba(255, 255, 255,0.3);\n"
"\n"
"}\n"
"\n"
"#downloadHistory_lw{\n"
"	background-color: transparent;\n"
"	border: 1px solid rgba(255, 255, 255,0.4)\n"
"\n"
"}\n"
"\n"
"\n"
"#link_button{\n"
"	"
                        "background-color: rgba(0, 0, 0,0.4);\n"
"	border: none;\n"
"	padding-right: 13px;\n"
"	padding-top: 2px;\n"
"\n"
"}\n"
"\n"
"\n"
"#URL_placement{\n"
"	border-radius: 10px;\n"
"	padding: 6px;\n"
"    min-height: 20px;\n"
"	background-color: rgba(59, 59, 59,0.7);\n"
"	border: 1px solid rgba(249, 249, 249,0.3);\n"
"}\n"
"#kuddos_bt{\n"
"	background-color: transparent;\n"
"	border: none;\n"
"}\n"
"\n"
"#kuddos_bt:hover{\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"#centralwidget {\n"
"    background-color: black;\n"
"}\n"
"\n"
"#Settings_BT{\n"
"	background-color: transparent;\n"
"	border: none;\n"
"}\n"
"\n"
"#Downloads_BT{\n"
"	background-color: transparent;\n"
"	border: none;\n"
"}\n"
"\n"
"\n"
"#goPage3_bt{\n"
"	border-radius: 14px;\n"
"	background-color: transparent;\n"
"	border: none;\n"
"}\n"
"\n"
"#goPage3_bt:hover {\n"
"	border-radius: 14px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"#BackHome_Downloads{\n"
"	background-color: transparent;\n"
"	border:none;\n"
"	border-radius: 5px;\n"
"\n"
""
                        "}\n"
"\n"
"#home_kudopage_bt{\n"
"	background-color: transparent;\n"
"	border:none;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#backHome_bt{\n"
"	background-color: transparent;\n"
"	border:none;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"#CheckURL_bt{\n"
"    background-color: rgba(0, 0, 0,0.7);\n"
"    color: white;\n"
"    font-size: 15px;\n"
"	text-align: center;\n"
"	border: 1px solid rgba(185, 185, 185,0.5);\n"
"	border-radius: 7px;\n"
"	padding: 4px;\n"
"}\n"
"\n"
"#CheckURL_bt:hover{\n"
"    background-color: rgba(100, 100, 100, 0.5);\n"
"    border: 1px solid #888;\n"
"}\n"
"\n"
"#CheckURL_bt:pressed{\n"
"    background-color: rgba(150, 150, 150, 0.5);\n"
"}\n"
"\n"
"#previewDownload_bt{\n"
"	background-color: rgba(26, 26, 26,0.7);\n"
"	border: 1px solid rgba(255, 255, 255,0.3);\n"
"\n"
"}\n"
"\n"
"#previewDownload_bt:hover{\n"
"	background-color: rgba(26, 26, 26,0.8);\n"
"	border: 1px solid rgba(255, 255, 255,0.6);\n"
"\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgba(0, 0, 0,0.8);\n"
"    c"
                        "olor: white;\n"
"    font-size: 15px;\n"
"	text-align: center;\n"
"	border: 1px solid white;\n"
"	border-radius: 7px;\n"
"	padding: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgba(100, 100, 100, 0.5);\n"
"    border: 1px solid #888;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgba(150, 150, 150, 0.5);\n"
"}\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mainVerticalLayout = QVBoxLayout(self.centralwidget)
        self.mainVerticalLayout.setObjectName(u"mainVerticalLayout")
        self.mainVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.pageHome = QWidget()
        self.pageHome.setObjectName(u"pageHome")
        self.pageHomeLayout = QVBoxLayout(self.pageHome)
        self.pageHomeLayout.setObjectName(u"pageHomeLayout")
        self.pageHomeLayout.setContentsMargins(3, 24, 10, 10)
        self.topSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.pageHomeLayout.addItem(self.topSpacer)

        self.centerRowLayout = QHBoxLayout()
        self.centerRowLayout.setObjectName(u"centerRowLayout")
        self.leftSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.centerRowLayout.addItem(self.leftSpacer)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.URL_placement = QLineEdit(self.pageHome)
        self.URL_placement.setObjectName(u"URL_placement")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.URL_placement.sizePolicy().hasHeightForWidth())
        self.URL_placement.setSizePolicy(sizePolicy)
        self.URL_placement.setMinimumSize(QSize(0, 34))

        self.gridLayout.addWidget(self.URL_placement, 3, 0, 1, 1)

        self.label1 = QLabel(self.pageHome)
        self.label1.setObjectName(u"label1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label1.sizePolicy().hasHeightForWidth())
        self.label1.setSizePolicy(sizePolicy1)
        self.label1.setMinimumSize(QSize(300, 0))
        font = QFont()
        font.setBold(True)
        self.label1.setFont(font)
        self.label1.setStyleSheet(u"")
        self.label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label1.setMargin(0)

        self.gridLayout.addWidget(self.label1, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 7, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 7, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 2, 0, 1, 1)

        self.CheckURL_bt = QPushButton(self.pageHome)
        self.CheckURL_bt.setObjectName(u"CheckURL_bt")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.CheckURL_bt.sizePolicy().hasHeightForWidth())
        self.CheckURL_bt.setSizePolicy(sizePolicy2)
        self.CheckURL_bt.setMinimumSize(QSize(150, 25))
        self.CheckURL_bt.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.gridLayout.addWidget(self.CheckURL_bt, 5, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.labelnew = QLabel(self.pageHome)
        self.labelnew.setObjectName(u"labelnew")
        font1 = QFont()
        font1.setBold(True)
        font1.setItalic(True)
        self.labelnew.setFont(font1)
        self.labelnew.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.labelnew, 1, 0, 1, 1)

        self.gridLayout.setRowStretch(0, 3)

        self.centerRowLayout.addLayout(self.gridLayout)

        self.rightSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.centerRowLayout.addItem(self.rightSpacer)

        self.centerRowLayout.setStretch(0, 5)
        self.centerRowLayout.setStretch(1, 19)
        self.centerRowLayout.setStretch(2, 5)

        self.pageHomeLayout.addLayout(self.centerRowLayout)

        self.bottomSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.pageHomeLayout.addItem(self.bottomSpacer)

        self.settinsNavLayout = QHBoxLayout()
        self.settinsNavLayout.setSpacing(1)
        self.settinsNavLayout.setObjectName(u"settinsNavLayout")
        self.Settings_BT = QPushButton(self.pageHome)
        self.Settings_BT.setObjectName(u"Settings_BT")
        icon1 = QIcon()
        icon1.addFile(u":/icons/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Settings_BT.setIcon(icon1)
        self.Settings_BT.setIconSize(QSize(35, 35))

        self.settinsNavLayout.addWidget(self.Settings_BT)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.settinsNavLayout.addItem(self.horizontalSpacer_3)


        self.pageHomeLayout.addLayout(self.settinsNavLayout)

        self.homeBottomNavLayout = QHBoxLayout()
        self.homeBottomNavLayout.setSpacing(4)
        self.homeBottomNavLayout.setObjectName(u"homeBottomNavLayout")
        self.horizontalSpacer_4 = QSpacerItem(4, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.homeBottomNavLayout.addItem(self.horizontalSpacer_4)

        self.Downloads_BT = QPushButton(self.pageHome)
        self.Downloads_BT.setObjectName(u"Downloads_BT")
        icon2 = QIcon()
        icon2.addFile(u":/icons/downloads.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Downloads_BT.setIcon(icon2)
        self.Downloads_BT.setIconSize(QSize(26, 26))

        self.homeBottomNavLayout.addWidget(self.Downloads_BT)

        self.homeBottomLeftSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.homeBottomNavLayout.addItem(self.homeBottomLeftSpacer)

        self.goPage3_bt = QPushButton(self.pageHome)
        self.goPage3_bt.setObjectName(u"goPage3_bt")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.goPage3_bt.sizePolicy().hasHeightForWidth())
        self.goPage3_bt.setSizePolicy(sizePolicy3)
        self.goPage3_bt.setMinimumSize(QSize(28, 28))
        self.goPage3_bt.setMaximumSize(QSize(32, 32))
        self.goPage3_bt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.goPage3_bt.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/Github_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.goPage3_bt.setIcon(icon3)
        self.goPage3_bt.setIconSize(QSize(50, 55))

        self.homeBottomNavLayout.addWidget(self.goPage3_bt)

        self.kuddos_bt = QPushButton(self.pageHome)
        self.kuddos_bt.setObjectName(u"kuddos_bt")
        self.kuddos_bt.setMinimumSize(QSize(28, 28))
        self.kuddos_bt.setMaximumSize(QSize(32, 32))
        self.kuddos_bt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/kuddos.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.kuddos_bt.setIcon(icon4)
        self.kuddos_bt.setIconSize(QSize(28, 27))

        self.homeBottomNavLayout.addWidget(self.kuddos_bt)


        self.pageHomeLayout.addLayout(self.homeBottomNavLayout)

        self.stackedWidget.addWidget(self.pageHome)
        self.pageInputPreview = QWidget()
        self.pageInputPreview.setObjectName(u"pageInputPreview")
        self.pageInputPreviewLayout = QHBoxLayout(self.pageInputPreview)
        self.pageInputPreviewLayout.setSpacing(16)
        self.pageInputPreviewLayout.setObjectName(u"pageInputPreviewLayout")
        self.pageInputPreviewLayout.setContentsMargins(24, 24, 24, 24)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.backHome_bt = QPushButton(self.pageInputPreview)
        self.backHome_bt.setObjectName(u"backHome_bt")
        sizePolicy3.setHeightForWidth(self.backHome_bt.sizePolicy().hasHeightForWidth())
        self.backHome_bt.setSizePolicy(sizePolicy3)
        self.backHome_bt.setMinimumSize(QSize(12, 28))
        self.backHome_bt.setMaximumSize(QSize(25, 16777215))
        self.backHome_bt.setStyleSheet(u"#backHome_bt:hover{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/back.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.backHome_bt.setIcon(icon5)
        self.backHome_bt.setIconSize(QSize(22, 22))

        self.verticalLayout_2.addWidget(self.backHome_bt)

        self.imagePlaceholder_lb = QLabel(self.pageInputPreview)
        self.imagePlaceholder_lb.setObjectName(u"imagePlaceholder_lb")
        self.imagePlaceholder_lb.setMinimumSize(QSize(360, 360))
        self.imagePlaceholder_lb.setMaximumSize(QSize(670, 430))
        self.imagePlaceholder_lb.setFrameShape(QFrame.Shape.Box)
        self.imagePlaceholder_lb.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.imagePlaceholder_lb)

        self.VideoInfoWid = QWidget(self.pageInputPreview)
        self.VideoInfoWid.setObjectName(u"VideoInfoWid")
        self.verticalLayout_7 = QVBoxLayout(self.VideoInfoWid)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label = QLabel(self.VideoInfoWid)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.label.setFont(font2)

        self.verticalLayout_7.addWidget(self.label)

        self.label_10 = QLabel(self.VideoInfoWid)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)

        self.verticalLayout_7.addWidget(self.label_10)

        self.label_9 = QLabel(self.VideoInfoWid)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)

        self.verticalLayout_7.addWidget(self.label_9)

        self.label_8 = QLabel(self.VideoInfoWid)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)

        self.verticalLayout_7.addWidget(self.label_8)


        self.verticalLayout_2.addWidget(self.VideoInfoWid)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.pageInputPreviewLayout.addLayout(self.verticalLayout_2)

        self.inputSideLayout = QVBoxLayout()
        self.inputSideLayout.setSpacing(12)
        self.inputSideLayout.setObjectName(u"inputSideLayout")
        self.optionslayout = QWidget(self.pageInputPreview)
        self.optionslayout.setObjectName(u"optionslayout")
        self.verticalLayout_6 = QVBoxLayout(self.optionslayout)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.inputTitle_lb = QLabel(self.optionslayout)
        self.inputTitle_lb.setObjectName(u"inputTitle_lb")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.inputTitle_lb.sizePolicy().hasHeightForWidth())
        self.inputTitle_lb.setSizePolicy(sizePolicy4)
        self.inputTitle_lb.setMinimumSize(QSize(70, 0))
        self.inputTitle_lb.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.inputTitle_lb.setMargin(1)

        self.verticalLayout_6.addWidget(self.inputTitle_lb)

        self.userInput_le = QLineEdit(self.optionslayout)
        self.userInput_le.setObjectName(u"userInput_le")
        sizePolicy.setHeightForWidth(self.userInput_le.sizePolicy().hasHeightForWidth())
        self.userInput_le.setSizePolicy(sizePolicy)
        self.userInput_le.setMinimumSize(QSize(0, 32))

        self.verticalLayout_6.addWidget(self.userInput_le)

        self.gridLayout_2_layout = QGridLayout()
        self.gridLayout_2_layout.setObjectName(u"gridLayout_2_layout")
        self.widget_2 = QWidget(self.optionslayout)
        self.widget_2.setObjectName(u"widget_2")

        self.gridLayout_2_layout.addWidget(self.widget_2, 2, 1, 1, 1)

        self.label_3 = QLabel(self.optionslayout)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout_2_layout.addWidget(self.label_3, 0, 1, 1, 1)

        self.comboBox_3 = QComboBox(self.optionslayout)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.gridLayout_2_layout.addWidget(self.comboBox_3, 4, 1, 1, 1)

        self.comboBox_2 = QComboBox(self.optionslayout)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout_2_layout.addWidget(self.comboBox_2, 1, 1, 1, 1)

        self.lineEdit = QLineEdit(self.optionslayout)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy5)

        self.gridLayout_2_layout.addWidget(self.lineEdit, 4, 0, 1, 1)

        self.label_2 = QLabel(self.optionslayout)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout_2_layout.addWidget(self.label_2, 0, 0, 1, 1)

        self.widget = QWidget(self.optionslayout)
        self.widget.setObjectName(u"widget")

        self.gridLayout_2_layout.addWidget(self.widget, 2, 0, 1, 1)

        self.label_5 = QLabel(self.optionslayout)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.gridLayout_2_layout.addWidget(self.label_5, 3, 1, 1, 1)

        self.comboBox = QComboBox(self.optionslayout)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_2_layout.addWidget(self.comboBox, 1, 0, 1, 1)

        self.label_4 = QLabel(self.optionslayout)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout_2_layout.addWidget(self.label_4, 3, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.optionslayout)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy5.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy5)

        self.gridLayout_2_layout.addWidget(self.lineEdit_2, 6, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.optionslayout)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy5.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy5)

        self.gridLayout_2_layout.addWidget(self.lineEdit_3, 6, 1, 1, 1)

        self.playlistType_lb = QLabel(self.optionslayout)
        self.playlistType_lb.setObjectName(u"playlistType_lb")
        self.playlistType_lb.setFont(font)

        self.gridLayout_2_layout.addWidget(self.playlistType_lb, 7, 0, 1, 1)

        self.playlistTypeValue_lb = QLabel(self.optionslayout)
        self.playlistTypeValue_lb.setObjectName(u"playlistTypeValue_lb")
        self.playlistTypeValue_lb.setFont(font)

        self.gridLayout_2_layout.addWidget(self.playlistTypeValue_lb, 7, 1, 1, 1)

        self.playlistScope_lb = QLabel(self.optionslayout)
        self.playlistScope_lb.setObjectName(u"playlistScope_lb")
        self.playlistScope_lb.setFont(font)

        self.gridLayout_2_layout.addWidget(self.playlistScope_lb, 8, 0, 1, 1)

        self.playlistScope_cb = QComboBox(self.optionslayout)
        self.playlistScope_cb.addItem("")
        self.playlistScope_cb.addItem("")
        self.playlistScope_cb.setObjectName(u"playlistScope_cb")
        sizePolicy5.setHeightForWidth(self.playlistScope_cb.sizePolicy().hasHeightForWidth())
        self.playlistScope_cb.setSizePolicy(sizePolicy5)
        self.playlistScope_cb.setMinimumSize(QSize(0, 0))
        font3 = QFont()
        font3.setPointSize(8)
        font3.setBold(True)
        self.playlistScope_cb.setFont(font3)

        self.gridLayout_2_layout.addWidget(self.playlistScope_cb, 8, 1, 1, 1)

        self.label_6 = QLabel(self.optionslayout)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2_layout.addWidget(self.label_6, 5, 0, 1, 2)


        self.verticalLayout_6.addLayout(self.gridLayout_2_layout)

        self.playlistBrowserWid = QWidget(self.optionslayout)
        self.playlistBrowserWid.setObjectName(u"playlistBrowserWid")
        self.playlistBrowserWid.setMinimumSize(QSize(0, 190))
        self.playlistBrowserWid.setMaximumSize(QSize(16777215, 190))
        self.playlistBrowserLayout = QVBoxLayout(self.playlistBrowserWid)
        self.playlistBrowserLayout.setSpacing(6)
        self.playlistBrowserLayout.setObjectName(u"playlistBrowserLayout")
        self.playlistBrowserLayout.setContentsMargins(0, 0, 0, 0)
        self.playlistBrowserTitle_lb = QLabel(self.playlistBrowserWid)
        self.playlistBrowserTitle_lb.setObjectName(u"playlistBrowserTitle_lb")
        self.playlistBrowserTitle_lb.setFont(font2)

        self.playlistBrowserLayout.addWidget(self.playlistBrowserTitle_lb)

        self.playlistThumbs_lw = QListWidget(self.playlistBrowserWid)
        self.playlistThumbs_lw.setObjectName(u"playlistThumbs_lw")
        self.playlistThumbs_lw.setMinimumSize(QSize(0, 130))
        self.playlistThumbs_lw.setMaximumSize(QSize(16777215, 130))

        self.playlistBrowserLayout.addWidget(self.playlistThumbs_lw)


        self.verticalLayout_6.addWidget(self.playlistBrowserWid)


        self.inputSideLayout.addWidget(self.optionslayout)

        self.previewDownload_bt = QPushButton(self.pageInputPreview)
        self.previewDownload_bt.setObjectName(u"previewDownload_bt")
        sizePolicy3.setHeightForWidth(self.previewDownload_bt.sizePolicy().hasHeightForWidth())
        self.previewDownload_bt.setSizePolicy(sizePolicy3)
        self.previewDownload_bt.setMinimumSize(QSize(300, 0))
        self.previewDownload_bt.setMaximumSize(QSize(340, 16777215))
        icon6 = QIcon()
        icon6.addFile(u":/icons/downloads2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.previewDownload_bt.setIcon(icon6)
        self.previewDownload_bt.setIconSize(QSize(60, 37))

        self.inputSideLayout.addWidget(self.previewDownload_bt, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.inputSideLayout.addItem(self.verticalSpacer_6)


        self.pageInputPreviewLayout.addLayout(self.inputSideLayout)

        self.pageInputPreviewLayout.setStretch(0, 2)
        self.pageInputPreviewLayout.setStretch(1, 1)
        self.stackedWidget.addWidget(self.pageInputPreview)
        self.pageEmpty = QWidget()
        self.pageEmpty.setObjectName(u"pageEmpty")
        self.pageEmptyLayout = QVBoxLayout(self.pageEmpty)
        self.pageEmptyLayout.setObjectName(u"pageEmptyLayout")
        self.pageEmptyLayout.setContentsMargins(0, 0, 0, 0)
        self.giflabel = QLabel(self.pageEmpty)
        self.giflabel.setObjectName(u"giflabel")
        self.giflabel.setScaledContents(True)
        self.gifOverlayLayout = QVBoxLayout(self.giflabel)
        self.gifOverlayLayout.setObjectName(u"gifOverlayLayout")
        self.gifOverlayLayout.setContentsMargins(10, 10, 10, 10)
        self.emptyContentWidget = QWidget(self.giflabel)
        self.emptyContentWidget.setObjectName(u"emptyContentWidget")
        self.horizontalLayout = QHBoxLayout(self.emptyContentWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.home_kudopage_bt = QPushButton(self.emptyContentWidget)
        self.home_kudopage_bt.setObjectName(u"home_kudopage_bt")
        sizePolicy2.setHeightForWidth(self.home_kudopage_bt.sizePolicy().hasHeightForWidth())
        self.home_kudopage_bt.setSizePolicy(sizePolicy2)
        self.home_kudopage_bt.setIcon(icon5)
        self.home_kudopage_bt.setIconSize(QSize(22, 22))

        self.verticalLayout.addWidget(self.home_kudopage_bt)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_8)

        self.label_7 = QLabel(self.emptyContentWidget)
        self.label_7.setObjectName(u"label_7")
        font4 = QFont()
        font4.setPointSize(40)
        font4.setBold(True)
        self.label_7.setFont(font4)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_7)

        self.label_11 = QLabel(self.emptyContentWidget)
        self.label_11.setObjectName(u"label_11")
        font5 = QFont()
        font5.setPointSize(18)
        font5.setBold(True)
        self.label_11.setFont(font5)
        self.label_11.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_11)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_9)

        self.label_12 = QLabel(self.emptyContentWidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setEnabled(True)
        font6 = QFont()
        font6.setPointSize(13)
        font6.setBold(True)
        self.label_12.setFont(font6)
        self.label_12.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_12)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_7)

        self.label_14 = QLabel(self.emptyContentWidget)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout.addWidget(self.label_14)

        self.guidance_label = QLabel(self.emptyContentWidget)
        self.guidance_label.setObjectName(u"guidance_label")
        self.guidance_label.setFont(font1)
        self.guidance_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.guidance_label)

        self.link_button = QPushButton(self.emptyContentWidget)
        self.link_button.setObjectName(u"link_button")
        sizePolicy3.setHeightForWidth(self.link_button.sizePolicy().hasHeightForWidth())
        self.link_button.setSizePolicy(sizePolicy3)
        self.link_button.setMinimumSize(QSize(360, 50))
        self.link_button.setMaximumSize(QSize(360, 31))
        font7 = QFont()
        self.link_button.setFont(font7)
        self.link_button.setStyleSheet(u"#link_button{\n"
"	background-color: rgba(0, 0, 0,0.4);\n"
"	border: none;\n"
"	padding-right: 13px;\n"
"	padding-top: 2px;\n"
"	font-size: 14px;\n"
"\n"
"}\n"
"\n"
"#link_button:hover{\n"
"	background-color: rgba(0, 0, 0,0.7);\n"
"	border: none;\n"
"	padding-right: 13px;\n"
"	padding-top: 2px;\n"
"	font-size: 14px;\n"
"\n"
"}")
        self.link_button.setIcon(icon3)
        self.link_button.setIconSize(QSize(55, 33))

        self.verticalLayout.addWidget(self.link_button, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(6, 1)

        self.horizontalLayout.addLayout(self.verticalLayout)


        self.gifOverlayLayout.addWidget(self.emptyContentWidget)


        self.pageEmptyLayout.addWidget(self.giflabel)

        self.stackedWidget.addWidget(self.pageEmpty)
        self.page_downloads = QWidget()
        self.page_downloads.setObjectName(u"page_downloads")
        self.horizontalLayout_2 = QHBoxLayout(self.page_downloads)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.BackHome_Downloads = QPushButton(self.page_downloads)
        self.BackHome_Downloads.setObjectName(u"BackHome_Downloads")
        self.BackHome_Downloads.setIcon(icon5)
        self.BackHome_Downloads.setIconSize(QSize(22, 22))

        self.horizontalLayout_4.addWidget(self.BackHome_Downloads)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.Downloads_info = QWidget(self.page_downloads)
        self.Downloads_info.setObjectName(u"Downloads_info")
        self.verticalLayout_8 = QVBoxLayout(self.Downloads_info)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.Thumbnail_placeholder = QLabel(self.Downloads_info)
        self.Thumbnail_placeholder.setObjectName(u"Thumbnail_placeholder")
        font8 = QFont()
        font8.setPointSize(23)
        self.Thumbnail_placeholder.setFont(font8)
        self.Thumbnail_placeholder.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.Thumbnail_placeholder)

        self.info_downloaded = QLabel(self.Downloads_info)
        self.info_downloaded.setObjectName(u"info_downloaded")
        font9 = QFont()
        font9.setPointSize(13)
        self.info_downloaded.setFont(font9)

        self.verticalLayout_8.addWidget(self.info_downloaded)


        self.verticalLayout_3.addWidget(self.Downloads_info)

        self.verticalLayout_3.setStretch(1, 1)

        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_13 = QLabel(self.page_downloads)
        self.label_13.setObjectName(u"label_13")
        font10 = QFont()
        font10.setPointSize(19)
        font10.setBold(True)
        self.label_13.setFont(font10)
        self.label_13.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_13)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.downloadHistory_lw = QListWidget(self.page_downloads)
        self.downloadHistory_lw.setObjectName(u"downloadHistory_lw")

        self.verticalLayout_5.addWidget(self.downloadHistory_lw)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_5)


        self.verticalLayout_4.addLayout(self.verticalLayout_5)

        self.verticalLayout_4.setStretch(0, 1)

        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.stackedWidget.addWidget(self.page_downloads)

        self.mainVerticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Cozydownloader", None))
        self.URL_placement.setPlaceholderText(QCoreApplication.translate("MainWindow", u"https://youtube.com/somerandomstuff", None))
        self.label1.setText(QCoreApplication.translate("MainWindow", u"Cozy downloader", None))
        self.CheckURL_bt.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.labelnew.setText(QCoreApplication.translate("MainWindow", u"Enter a video or playlist URL to download it", None))
        self.Settings_BT.setText("")
        self.Downloads_BT.setText("")
        self.goPage3_bt.setText("")
        self.kuddos_bt.setText("")
        self.backHome_bt.setText("")
        self.imagePlaceholder_lb.setText(QCoreApplication.translate("MainWindow", u"Image Placeholder", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"VideoTitle: ", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"VideoSize:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Duration:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"ViewCount:", None))
        self.inputTitle_lb.setText(QCoreApplication.translate("MainWindow", u"User Input", None))
        self.userInput_le.setPlaceholderText(QCoreApplication.translate("MainWindow", u"User input", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.playlistType_lb.setText(QCoreApplication.translate("MainWindow", u"Detected link type", None))
        self.playlistTypeValue_lb.setText(QCoreApplication.translate("MainWindow", u"Unknown", None))
        self.playlistScope_lb.setText(QCoreApplication.translate("MainWindow", u"Download scope", None))
        self.playlistScope_cb.setItemText(0, QCoreApplication.translate("MainWindow", u"Only current video (default)", None))
        self.playlistScope_cb.setItemText(1, QCoreApplication.translate("MainWindow", u"Full playlist", None))

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.playlistBrowserTitle_lb.setText(QCoreApplication.translate("MainWindow", u"Playlist videos", None))
        self.previewDownload_bt.setText("")
        self.giflabel.setText("")
        self.home_kudopage_bt.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Thank you", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"for downloading with Cozy downloader", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"made by: cozidesire", None))
        self.label_14.setText("")
        self.guidance_label.setText(QCoreApplication.translate("MainWindow", u"Click the link below for access to the repository for new versions and updates", None))
        self.link_button.setText(QCoreApplication.translate("MainWindow", u"https://github.com/cozidesire/cozydownloader", None))
        self.BackHome_Downloads.setText("")
        self.Thumbnail_placeholder.setText(QCoreApplication.translate("MainWindow", u"No video selected", None))
        self.info_downloaded.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Your Downloads: ", None))
    # retranslateUi

