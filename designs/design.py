# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1219, 856)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(3)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/detection.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(-10, 0, 1231, 841))
        font = QtGui.QFont()
        font.setFamily("Segoe WP Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setStyleSheet("QStackedWidget#login_page{\n"
"background-color: #464646;\n"
"}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.first_page = QtWidgets.QWidget()
        self.first_page.setStyleSheet("QWidget#first_page{\n"
"background-color: #464646;\n"
"}")
        self.first_page.setObjectName("first_page")
        self.menuBox = QtWidgets.QGroupBox(self.first_page)
        self.menuBox.setGeometry(QtCore.QRect(10, 0, 271, 841))
        self.menuBox.setStyleSheet("QGroupBox{\n"
"border: none;\n"
"background-color: #2f2f2f;\n"
"}")
        self.menuBox.setTitle("")
        self.menuBox.setObjectName("menuBox")
        self.usernotifications = QtWidgets.QPushButton(self.menuBox)
        self.usernotifications.setGeometry(QtCore.QRect(0, 130, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.usernotifications.setFont(font)
        self.usernotifications.setStyleSheet("QPushButton#usernotifications{\n"
"    background-color: Transparent;\n"
"    background-repeat:no-repeat;\n"
"color: white;\n"
"    border: none;\n"
"\n"
"    outline:none;\n"
"    Text-align:left;\n"
"padding-left: 20px;\n"
"}\n"
"QPushButton:hover#usernotifications{\n"
" background-color: #5e5e5e;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./images/notification.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.usernotifications.setIcon(icon1)
        self.usernotifications.setIconSize(QtCore.QSize(23, 23))
        self.usernotifications.setObjectName("usernotifications")
        self.webcamDetect = QtWidgets.QPushButton(self.menuBox)
        self.webcamDetect.setGeometry(QtCore.QRect(0, 180, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe WP Semibold")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.webcamDetect.setFont(font)
        self.webcamDetect.setStyleSheet("QPushButton#webcamDetect{\n"
"    background-color: Transparent;\n"
"    background-repeat:no-repeat;\n"
"    border: none;\n"
"\n"
"color: white;\n"
"    outline:none;\n"
"    Text-align:left;\n"
"padding-left: 20px;\n"
"}\n"
"QPushButton:hover#webcamDetect{\n"
" background-color: #5e5e5e;\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./images/webcamdetect.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.webcamDetect.setIcon(icon2)
        self.webcamDetect.setIconSize(QtCore.QSize(22, 22))
        self.webcamDetect.setObjectName("webcamDetect")
        self.detectimage = QtWidgets.QPushButton(self.menuBox)
        self.detectimage.setGeometry(QtCore.QRect(0, 230, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe WP Semibold")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.detectimage.setFont(font)
        self.detectimage.setStyleSheet("QPushButton#detectimage{\n"
"    background-color: Transparent;\n"
"    background-repeat:no-repeat;\n"
"    border: none;\n"
"    cursor:pointer;\n"
"color: white;\n"
"    Text-align:left;\n"
"padding-left: 20px;\n"
"}\n"
"QPushButton:hover#detectimage{\n"
" background-color: #5e5e5e;\n"
"\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./images/Dslr-Camera-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.detectimage.setIcon(icon3)
        self.detectimage.setIconSize(QtCore.QSize(23, 23))
        self.detectimage.setObjectName("detectimage")
        self.detectvideo = QtWidgets.QPushButton(self.menuBox)
        self.detectvideo.setGeometry(QtCore.QRect(0, 280, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.detectvideo.setFont(font)
        self.detectvideo.setStyleSheet("QPushButton#detectvideo{\n"
"    background-color: Transparent;\n"
"    background-repeat:no-repeat;\n"
"    border: none;\n"
"    cursor:pointer;\n"
"color: white;\n"
"    Text-align:left;\n"
"padding-left: 20px;\n"
"}\n"
"QPushButton:hover#detectvideo{\n"
" background-color: #5e5e5e;\n"
"\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("./images/folder-red-video-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.detectvideo.setIcon(icon4)
        self.detectvideo.setIconSize(QtCore.QSize(25, 25))
        self.detectvideo.setObjectName("detectvideo")
        self.userSettings = QtWidgets.QPushButton(self.menuBox)
        self.userSettings.setGeometry(QtCore.QRect(0, 330, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.userSettings.setFont(font)
        self.userSettings.setStyleSheet("QPushButton#userSettings{\n"
"    background-color: Transparent;\n"
"    background-repeat:no-repeat;\n"
"    border: none;\n"
"color: white;\n"
"    outline:none;\n"
"    Text-align:left;\n"
"padding-left: 22px;\n"
"}\n"
"QPushButton:hover#userSettings{\n"
" background-color: #5e5e5e;\n"
"}")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("./images/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.userSettings.setIcon(icon5)
        self.userSettings.setIconSize(QtCore.QSize(23, 23))
        self.userSettings.setObjectName("userSettings")
        self.logout = QtWidgets.QPushButton(self.menuBox)
        self.logout.setGeometry(QtCore.QRect(0, 380, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.logout.setFont(font)
        self.logout.setStyleSheet("QPushButton#logout{\n"
"    background-color: Transparent;\n"
"    background-repeat:no-repeat;\n"
"    border: none;\n"
"    outline:none;\n"
"    Text-align:left;\n"
"color: white;\n"
"padding-left: 18px;\n"
"}\n"
"QPushButton:hover#logout{\n"
" background-color: #5e5e5e;\n"
"}")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("./images/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logout.setIcon(icon6)
        self.logout.setIconSize(QtCore.QSize(30, 30))
        self.logout.setObjectName("logout")
        self.smokeTitle = QtWidgets.QPushButton(self.menuBox)
        self.smokeTitle.setGeometry(QtCore.QRect(10, 20, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.smokeTitle.setFont(font)
        self.smokeTitle.setStyleSheet("QPushButton#smokeTitle{\n"
"    background-color: Transparent;\n"
"    background-repeat:no-repeat;\n"
"    color: white;\n"
"    border: none;\n"
"    outline:none;\n"
"    Text-align:left;\n"
"    padding-left: 20px;\n"
"}\n"
"")
        self.smokeTitle.setIcon(icon)
        self.smokeTitle.setIconSize(QtCore.QSize(25, 25))
        self.smokeTitle.setObjectName("smokeTitle")
        self.line_2 = QtWidgets.QFrame(self.menuBox)
        self.line_2.setGeometry(QtCore.QRect(20, 168, 221, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.menuBox)
        self.line_3.setGeometry(QtCore.QRect(20, 218, 221, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.menuBox)
        self.line_4.setGeometry(QtCore.QRect(20, 268, 221, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.menuBox)
        self.line_5.setGeometry(QtCore.QRect(20, 318, 221, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.menuBox)
        self.line_6.setGeometry(QtCore.QRect(20, 368, 221, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.stackedWidget_4 = QtWidgets.QStackedWidget(self.menuBox)
        self.stackedWidget_4.setGeometry(QtCore.QRect(10, 440, 251, 381))
        self.stackedWidget_4.setStyleSheet("QStackedWidget#stackedWidget_4{\n"
"border: none;\n"
"background-color: #2f2f2f;\n"
"}")
        self.stackedWidget_4.setObjectName("stackedWidget_4")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.stackedWidget_4.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.label_34 = QtWidgets.QLabel(self.page_5)
        self.label_34.setGeometry(QtCore.QRect(0, 20, 251, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe WP Semibold")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("QLabel#label_34{\n"
"    color: white;\n"
"}")
        self.label_34.setAlignment(QtCore.Qt.AlignCenter)
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.page_5)
        self.label_35.setGeometry(QtCore.QRect(10, 80, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_35.setFont(font)
        self.label_35.setStyleSheet("QLabel{\n"
"color: white;\n"
"}")
        self.label_35.setObjectName("label_35")
        self.checkBox = QtWidgets.QCheckBox(self.page_5)
        self.checkBox.setGeometry(QtCore.QRect(30, 100, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("QCheckBox\n"
"{\n"
"color: white;\n"
"}")
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.page_5)
        self.checkBox_2.setGeometry(QtCore.QRect(30, 120, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setStyleSheet("QCheckBox{\n"
"color: white;\n"
"}")
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.page_5)
        self.checkBox_3.setGeometry(QtCore.QRect(30, 140, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setStyleSheet("QCheckBox{\n"
"color: white;\n"
"}")
        self.checkBox_3.setObjectName("checkBox_3")
        self.label_36 = QtWidgets.QLabel(self.page_5)
        self.label_36.setGeometry(QtCore.QRect(10, 190, 241, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe WP Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet("QLabel{\n"
"color: white;\n"
"}")
        self.label_36.setObjectName("label_36")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.page_5)
        self.dateEdit_2.setGeometry(QtCore.QRect(10, 220, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe WP Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.dateEdit_2.setFont(font)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.dateEdit_3 = QtWidgets.QDateEdit(self.page_5)
        self.dateEdit_3.setGeometry(QtCore.QRect(150, 220, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe WP Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.dateEdit_3.setFont(font)
        self.dateEdit_3.setObjectName("dateEdit_3")
        self.label_37 = QtWidgets.QLabel(self.page_5)
        self.label_37.setGeometry(QtCore.QRect(110, 220, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe WP Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_37.setFont(font)
        self.label_37.setStyleSheet("QLabel{\n"
"color: white;\n"
"}")
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.filterbtn = QtWidgets.QPushButton(self.page_5)
        self.filterbtn.setGeometry(QtCore.QRect(30, 330, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.filterbtn.setFont(font)
        self.filterbtn.setStyleSheet("QPushButton#filterbtn{\n"
"    background-color: Transparent;\n"
"    background-repeat:no-repeat;\n"
"       border: 2px solid white;\n"
"    color: white;\n"
"border-radius:8px;\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover#filterbtn{\n"
"    background-color: white;\n"
"    border-color: white;\n"
"    color: black;\n"
"border-radius: 8px;\n"
"    border: 2px solid white;\n"
"}")
        self.filterbtn.setObjectName("filterbtn")
        self.label_38 = QtWidgets.QLabel(self.page_5)
        self.label_38.setGeometry(QtCore.QRect(10, 250, 241, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe WP Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_38.setFont(font)
        self.label_38.setStyleSheet("QLabel{\n"
"color: white;\n"
"}")
        self.label_38.setObjectName("label_38")
        self.stackedWidget_4.addWidget(self.page_5)
        self.line_9 = QtWidgets.QFrame(self.menuBox)
        self.line_9.setGeometry(QtCore.QRect(20, 118, 221, 16))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.homebutton = QtWidgets.QPushButton(self.menuBox)
        self.homebutton.setGeometry(QtCore.QRect(0, 80, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.homebutton.setFont(font)
        self.homebutton.setStyleSheet("QPushButton#homebutton{\n"
"    background-color: Transparent;\n"
"    background-repeat:no-repeat;\n"
"color: white;\n"
"    border: none;\n"
"\n"
"    outline:none;\n"
"    Text-align:left;\n"
"padding-left: 20px;\n"
"}\n"
"QPushButton:hover#homebutton{\n"
" background-color: #5e5e5e;\n"
"}")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("./images/house.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.homebutton.setIcon(icon7)
        self.homebutton.setIconSize(QtCore.QSize(23, 23))
        self.homebutton.setObjectName("homebutton")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.first_page)
        self.stackedWidget_2.setGeometry(QtCore.QRect(283, 10, 941, 821))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.stackedWidget_2.setFont(font)
        self.stackedWidget_2.setStyleSheet("QStackedWidget#stackedWidget_2{\n"
"background-color: #464646;\n"
"}")
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.setting_page = QtWidgets.QWidget()
        self.setting_page.setObjectName("setting_page")
        self.changeUserInfobtn = QtWidgets.QPushButton(self.setting_page)
        self.changeUserInfobtn.setGeometry(QtCore.QRect(90, 90, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe WP Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.changeUserInfobtn.setFont(font)
        self.changeUserInfobtn.setStyleSheet("QPushButton#changeUserInfobtn{\n"
"    background-color: Transparent;\n"
"    background-repeat:no-repeat;\n"
"    border: none;\n"
"    color: white;\n"
"    outline:none;\n"
"    \n"
"}\n"
"QPushButton:hover#changeUserInfobtn{\n"
"     text-decoration: underline;\n"
"    \n"
"}")
        self.changeUserInfobtn.setObjectName("changeUserInfobtn")
        self.Changepasswordbtn = QtWidgets.QPushButton(self.setting_page)
        self.Changepasswordbtn.setGeometry(QtCore.QRect(270, 90, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Changepasswordbtn.setFont(font)
        self.Changepasswordbtn.setStyleSheet("QPushButton#Changepasswordbtn{\n"
"    background-color: Transparent;\n"
"    background-repeat:no-repeat;\n"
"    border: none;\n"
"    color: white;\n"
"    outline:none;\n"
"    \n"
"}\n"
"QPushButton:hover#Changepasswordbtn{\n"
"     text-decoration: underline;\n"
"    \n"
"}")
        self.Changepasswordbtn.setObjectName("Changepasswordbtn")
        self.stackedWidget_3 = QtWidgets.QStackedWidget(self.setting_page)
        self.stackedWidget_3.setGeometry(QtCore.QRect(10, 150, 581, 391))
        self.stackedWidget_3.setStyleSheet("QStackedWidget#stackedWidget_3{\n"
"background-color: #464646;\n"
"}")
        self.stackedWidget_3.setObjectName("stackedWidget_3")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_5.setGeometry(QtCore.QRect(50, 160, 241, 31))
        self.lineEdit_5.setStyleSheet("QLineEdit#lineEdit_5{\n"
"border-radius:8px;\n"
"padding-left: 5px;\n"
"}")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_28 = QtWidgets.QLabel(self.page)
        self.label_28.setGeometry(QtCore.QRect(50, 140, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("QLabel#label_28{\n"
"color: white;\n"
"}")
        self.label_28.setObjectName("label_28")
        self.label_16 = QtWidgets.QLabel(self.page)
        self.label_16.setGeometry(QtCore.QRect(50, 20, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe WP Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("QLabel#label_16{\n"
"color: white;\n"
"}")
        self.label_16.setObjectName("label_16")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_3.setGeometry(QtCore.QRect(50, 40, 241, 31))
        self.lineEdit_3.setStyleSheet("QLineEdit#lineEdit_3{\n"
"border-radius:8px;\n"
"padding-left: 5px;\n"
"}")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_4.setGeometry(QtCore.QRect(50, 100, 241, 31))
        self.lineEdit_4.setStyleSheet("QLineEdit#lineEdit_4{\n"
"border-radius:8px;\n"
"padding-left: 5px;\n"
"}")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_22 = QtWidgets.QLabel(self.page)
        self.label_22.setGeometry(QtCore.QRect(50, 80, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("QLabel#label_22{\n"
"color: white;\n"
"}")
        self.label_22.setObjectName("label_22")
        self.saveuserinfobtn = QtWidgets.QPushButton(self.page)
        self.saveuserinfobtn.setGeometry(QtCore.QRect(250, 260, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.saveuserinfobtn.setFont(font)
        self.saveuserinfobtn.setStyleSheet("QPushButton#saveuserinfobtn{\n"
"    background-color: Transparent;\n"
"    background-repeat:no-repeat;\n"
"       border: 2px solid white;\n"
"    color: white;\n"
"border-radius:8px;\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover#saveuserinfobtn{\n"
"    background-color: white;\n"
"    border-color: white;\n"
"    color: black;\n"
"border-radius: 8px;\n"
"    border: 2px solid white;\n"
"}")
        self.saveuserinfobtn.setObjectName("saveuserinfobtn")
        self.stackedWidget_3.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_29 = QtWidgets.QLabel(self.page_2)
        self.label_29.setGeometry(QtCore.QRect(50, 20, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("QLabel#label_29{\n"
"color: white;\n"
"}")
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.page_2)
        self.label_30.setGeometry(QtCore.QRect(50, 80, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe WP Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("QLabel#label_30{\n"
"color: white;\n"
"}")
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.page_2)
        self.label_31.setGeometry(QtCore.QRect(50, 140, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe WP Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("QLabel#label_31{\n"
"color: white;\n"
"}")
        self.label_31.setObjectName("label_31")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_7.setGeometry(QtCore.QRect(50, 100, 241, 31))
        self.lineEdit_7.setStyleSheet("QLineEdit#lineEdit_7{\n"
"border-radius:8px;\n"
"padding-left: 5px;\n"
"}")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_8.setGeometry(QtCore.QRect(50, 160, 241, 31))
        self.lineEdit_8.setStyleSheet("QLineEdit#lineEdit_8{\n"
"border-radius:8px;\n"
"padding-left: 5px;\n"
"}")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(50, 40, 241, 31))
        self.lineEdit_6.setStyleSheet("QLineEdit#lineEdit_6{\n"
"border-radius:8px;\n"
"padding-left: 5px;\n"
"}")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.savenewpasswordbtn = QtWidgets.QPushButton(self.page_2)
        self.savenewpasswordbtn.setGeometry(QtCore.QRect(250, 260, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe WP Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.savenewpasswordbtn.setFont(font)
        self.savenewpasswordbtn.setStyleSheet("QPushButton#savenewpasswordbtn{\n"
"    background-color: Transparent;\n"
"    background-repeat:no-repeat;\n"
"       border: 2px solid white;\n"
"    color: white;\n"
"border-radius:8px;\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover#savenewpasswordbtn{\n"
"    background-color: white;\n"
"    border-color: white;\n"
"    color: black;\n"
"border-radius: 8px;\n"
"    border: 2px solid white;\n"
"}")
        self.savenewpasswordbtn.setObjectName("savenewpasswordbtn")
        self.errorlabel = QtWidgets.QLabel(self.page_2)
        self.errorlabel.setGeometry(QtCore.QRect(80, 210, 441, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.errorlabel.setFont(font)
        self.errorlabel.setStyleSheet("QLabel#errorlabel{\n"
"    color: red;\n"
"}")
        self.errorlabel.setText("")
        self.errorlabel.setObjectName("errorlabel")
        self.stackedWidget_3.addWidget(self.page_2)
        self.line_8 = QtWidgets.QFrame(self.setting_page)
        self.line_8.setGeometry(QtCore.QRect(250, 90, 20, 31))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.stackedWidget_2.addWidget(self.setting_page)
        self.notification_page = QtWidgets.QWidget()
        self.notification_page.setObjectName("notification_page")
        self.label_7 = QtWidgets.QLabel(self.notification_page)
        self.label_7.setGeometry(QtCore.QRect(10, 0, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("QLabel#label_7{\n"
"color: white;\n"
"}")
        self.label_7.setObjectName("label_7")
        self.listWidget_2 = QtWidgets.QListWidget(self.notification_page)
        self.listWidget_2.setGeometry(QtCore.QRect(10, 30, 921, 781))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_2.sizePolicy().hasHeightForWidth())
        self.listWidget_2.setSizePolicy(sizePolicy)
        self.listWidget_2.setStyleSheet("QListWidget#listWidget_2{\n"
"background-color: Transparent;\n"
"    background-repeat:no-repeat;\n"
"border: none;\n"
"}")
        self.listWidget_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget_2.setFlow(QtWidgets.QListView.LeftToRight)
        self.listWidget_2.setProperty("isWrapping", True)
        self.listWidget_2.setObjectName("listWidget_2")
        self.stackedWidget_2.addWidget(self.notification_page)
        self.largeImage = QtWidgets.QWidget()
        self.largeImage.setObjectName("largeImage")
        self.backToNotification = QtWidgets.QPushButton(self.largeImage)
        self.backToNotification.setGeometry(QtCore.QRect(40, 20, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.backToNotification.setFont(font)
        self.backToNotification.setStyleSheet("QPushButton#backToNotification{\n"
"    background-color: Transparent;\n"
"    background-repeat:no-repeat;\n"
"    border: none;\n"
"\n"
"color: white;\n"
"    outline:none;\n"
"    Text-align:left;\n"
"padding-left: 20px;\n"
"}\n"
"\n"
"QPushButton:hover#backToNotification{\n"
"color: blue;\n"
"}\n"
"")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("./images/left-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backToNotification.setIcon(icon8)
        self.backToNotification.setIconSize(QtCore.QSize(30, 30))
        self.backToNotification.setObjectName("backToNotification")
        self.label_6 = QtWidgets.QLabel(self.largeImage)
        self.label_6.setGeometry(QtCore.QRect(240, 20, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("QLabel#label_6{\n"
"color: white;\n"
"}")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_32 = QtWidgets.QLabel(self.largeImage)
        self.label_32.setGeometry(QtCore.QRect(460, 20, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("QLabel#label_32{\n"
"color: white;\n"
"}")
        self.label_32.setText("")
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.largeImage)
        self.label_33.setGeometry(QtCore.QRect(720, 20, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("QLabel#label_33{\n"
"color: white;\n"
"}")
        self.label_33.setText("")
        self.label_33.setObjectName("label_33")
        self.enlargeImagelabel = QtWidgets.QLabel(self.largeImage)
        self.enlargeImagelabel.setGeometry(QtCore.QRect(80, 90, 831, 691))
        self.enlargeImagelabel.setText("")
        self.enlargeImagelabel.setObjectName("enlargeImagelabel")
        self.stackedWidget_2.addWidget(self.largeImage)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.label_39 = QtWidgets.QLabel(self.page_6)
        self.label_39.setGeometry(QtCore.QRect(30, 50, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_39.setFont(font)
        self.label_39.setStyleSheet("QLabel#label_39{\n"
"color: white;\n"
"}")
        self.label_39.setObjectName("label_39")
        self.label_41 = QtWidgets.QLabel(self.page_6)
        self.label_41.setGeometry(QtCore.QRect(60, 150, 261, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_41.setFont(font)
        self.label_41.setStyleSheet("QLabel#label_41{\n"
"color: white;\n"
"}")
        self.label_41.setObjectName("label_41")
        self.label_42 = QtWidgets.QLabel(self.page_6)
        self.label_42.setGeometry(QtCore.QRect(90, 190, 531, 41))
        self.label_42.setStyleSheet("QLabel#label_42{\n"
"color: white;\n"
"}")
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(self.page_6)
        self.label_43.setGeometry(QtCore.QRect(90, 230, 741, 51))
        self.label_43.setStyleSheet("QLabel#label_43{\n"
"color: white;\n"
"}")
        self.label_43.setObjectName("label_43")
        self.label_44 = QtWidgets.QLabel(self.page_6)
        self.label_44.setGeometry(QtCore.QRect(90, 280, 711, 41))
        self.label_44.setStyleSheet("QLabel#label_44{\n"
"color: white;\n"
"}")
        self.label_44.setObjectName("label_44")
        self.label_45 = QtWidgets.QLabel(self.page_6)
        self.label_45.setGeometry(QtCore.QRect(90, 330, 721, 41))
        self.label_45.setStyleSheet("QLabel#label_45{\n"
"color: white;\n"
"}")
        self.label_45.setObjectName("label_45")
        self.label_46 = QtWidgets.QLabel(self.page_6)
        self.label_46.setGeometry(QtCore.QRect(90, 380, 721, 41))
        self.label_46.setText("")
        self.label_46.setObjectName("label_46")
        self.label_47 = QtWidgets.QLabel(self.page_6)
        self.label_47.setGeometry(QtCore.QRect(60, 390, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_47.setFont(font)
        self.label_47.setStyleSheet("QLabel#label_47{\n"
"color: white;\n"
"}")
        self.label_47.setObjectName("label_47")
        self.label_48 = QtWidgets.QLabel(self.page_6)
        self.label_48.setGeometry(QtCore.QRect(90, 520, 701, 31))
        self.label_48.setStyleSheet("QLabel#label_48{\n"
"color: white;\n"
"}")
        self.label_48.setObjectName("label_48")
        self.label_49 = QtWidgets.QLabel(self.page_6)
        self.label_49.setGeometry(QtCore.QRect(90, 470, 711, 31))
        self.label_49.setStyleSheet("QLabel#label_49{\n"
"color: white;\n"
"}")
        self.label_49.setObjectName("label_49")
        self.label_50 = QtWidgets.QLabel(self.page_6)
        self.label_50.setGeometry(QtCore.QRect(90, 420, 711, 41))
        self.label_50.setStyleSheet("QLabel#label_50{\n"
"color: white;\n"
"}")
        self.label_50.setObjectName("label_50")
        self.label_51 = QtWidgets.QLabel(self.page_6)
        self.label_51.setGeometry(QtCore.QRect(90, 560, 721, 41))
        self.label_51.setStyleSheet("QLabel#label_51{\n"
"color: white;\n"
"}")
        self.label_51.setObjectName("label_51")
        self.label_52 = QtWidgets.QLabel(self.page_6)
        self.label_52.setGeometry(QtCore.QRect(90, 610, 721, 41))
        self.label_52.setStyleSheet("QLabel#label_52{\n"
"color: white;\n"
"}")
        self.label_52.setObjectName("label_52")
        self.label_53 = QtWidgets.QLabel(self.page_6)
        self.label_53.setGeometry(QtCore.QRect(90, 660, 721, 41))
        self.label_53.setStyleSheet("QLabel#label_53{\n"
"color: white;\n"
"}")
        self.label_53.setObjectName("label_53")
        self.label_54 = QtWidgets.QLabel(self.page_6)
        self.label_54.setGeometry(QtCore.QRect(90, 710, 721, 41))
        self.label_54.setStyleSheet("QLabel#label_54{\n"
"color: white;\n"
"}")
        self.label_54.setObjectName("label_54")
        self.stackedWidget_2.addWidget(self.page_6)
        self.detect_image_page = QtWidgets.QWidget()
        self.detect_image_page.setStyleSheet("")
        self.detect_image_page.setObjectName("detect_image_page")
        self.openFilebtn = QtWidgets.QPushButton(self.detect_image_page)
        self.openFilebtn.setGeometry(QtCore.QRect(230, 60, 82, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe WP Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.openFilebtn.setFont(font)
        self.openFilebtn.setStyleSheet("QPushButton#openFilebtn{\n"
"    background-color: Transparent;\n"
"    background-repeat:no-repeat;\n"
"       border: 2px solid white;\n"
"    color: white;\n"
"border-radius:8px;\n"
"\n"
"}\n"
"QPushButton:hover#openFilebtn{\n"
"    background-color: white;\n"
"    border-color: white;\n"
"    color: black;\n"
"    border: 2px solid white;\n"
"border-radius: 8px;\n"
"}")
        self.openFilebtn.setObjectName("openFilebtn")
        self.imagedetectbtn = QtWidgets.QPushButton(self.detect_image_page)
        self.imagedetectbtn.setGeometry(QtCore.QRect(330, 710, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe WP Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.imagedetectbtn.setFont(font)
        self.imagedetectbtn.setStyleSheet("QPushButton#imagedetectbtn{\n"
"    background-color: Transparent;\n"
"    background-repeat:no-repeat;\n"
"    border: 2px solid white;\n"
"    color: white;\n"
"border-radius:8px;\n"
"\n"
"}\n"
"QPushButton:hover#imagedetectbtn{\n"
"    background-color: white;\n"
"    border-color: white;\n"
"    color: black;\n"
"border-radius: 8px;\n"
"    border: 2px solid white;\n"
"}")
        self.imagedetectbtn.setObjectName("imagedetectbtn")
        self.label_11 = QtWidgets.QLabel(self.detect_image_page)
        self.label_11.setGeometry(QtCore.QRect(130, 130, 641, 551))
        font = QtGui.QFont()
        font.setFamily("Segoe WP Semibold")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("QLabel#label_11{\n"
"color: white;\n"
"}")
        self.label_11.setTextFormat(QtCore.Qt.AutoText)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.detect_image_page)
        self.label_12.setGeometry(QtCore.QRect(120, 0, 681, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("QLabel#label_12{\n"
"color: white;\n"
"}")
        self.label_12.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_12.setObjectName("label_12")
        self.setPathbtn = QtWidgets.QPushButton(self.detect_image_page)
        self.setPathbtn.setGeometry(QtCore.QRect(230, 90, 82, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.setPathbtn.setFont(font)
        self.setPathbtn.setStyleSheet("QPushButton#setPathbtn{\n"
"    background-color: Transparent;\n"
"    background-repeat:no-repeat;\n"
"    border: 2px solid white;\n"
"    color: white;\n"
"border-radius:8px;\n"
"\n"
"}\n"
"QPushButton:hover#setPathbtn{\n"
"    background-color: white;\n"
"    border-color: white;\n"
"    color: black;\n"
"border-radius: 8px;\n"
"    border: 2px solid white;\n"
"}")
        self.setPathbtn.setObjectName("setPathbtn")
        self.fileLabel = QtWidgets.QLabel(self.detect_image_page)
        self.fileLabel.setGeometry(QtCore.QRect(320, 62, 341, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe WP Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.fileLabel.setFont(font)
        self.fileLabel.setStyleSheet("QLabel#fileLabel{\n"
"color: white;\n"
"border-radius:4px;\n"
"  border: 2px solid white;\n"
"}")
        self.fileLabel.setObjectName("fileLabel")
        self.pathLabel = QtWidgets.QLabel(self.detect_image_page)
        self.pathLabel.setGeometry(QtCore.QRect(320, 92, 341, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pathLabel.setFont(font)
        self.pathLabel.setStyleSheet("QLabel#pathLabel{\n"
"color: white;\n"
"  border: 2px solid white;\n"
"border-radius:4px;\n"
"}")
        self.pathLabel.setObjectName("pathLabel")
        self.saveNotificationsImage = QtWidgets.QCheckBox(self.detect_image_page)
        self.saveNotificationsImage.setGeometry(QtCore.QRect(370, 680, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe WP Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.saveNotificationsImage.setFont(font)
        self.saveNotificationsImage.setStyleSheet("QCheckBox{\n"
"color: white;\n"
"}")
        self.saveNotificationsImage.setObjectName("saveNotificationsImage")
        self.label_21 = QtWidgets.QLabel(self.detect_image_page)
        self.label_21.setGeometry(QtCore.QRect(302, 750, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("QLabel#label_21{\n"
"color: white;\n"
"}")
        self.label_21.setText("")
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.stackedWidget_2.addWidget(self.detect_image_page)
        self.detect_video_page = QtWidgets.QWidget()
        self.detect_video_page.setObjectName("detect_video_page")
        self.saveNotificationsImage_3 = QtWidgets.QCheckBox(self.detect_video_page)
        self.saveNotificationsImage_3.setGeometry(QtCore.QRect(330, 470, 241, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe WP Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.saveNotificationsImage_3.setFont(font)
        self.saveNotificationsImage_3.setStyleSheet("QCheckBox{\n"
"color: white;\n"
"}")
        self.saveNotificationsImage_3.setObjectName("saveNotificationsImage_3")
        self.detectCamera_2 = QtWidgets.QPushButton(self.detect_video_page)
        self.detectCamera_2.setGeometry(QtCore.QRect(320, 510, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe WP Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.detectCamera_2.setFont(font)
        self.detectCamera_2.setStyleSheet("QPushButton#detectCamera_2{\n"
"    background-color: Transparent;\n"
"    background-repeat:no-repeat;\n"
"    border: 2px solid white;\n"
"    color: white;\n"
"border-radius:8px;\n"
"\n"
"}\n"
"QPushButton:hover#detectCamera_2{\n"
"    background-color: white;\n"
"    border-color: white;\n"
"    color: black;\n"
"border-radius: 8px;\n"
"    border: 2px solid white;\n"
"}")
        self.detectCamera_2.setObjectName("detectCamera_2")
        self.label_20 = QtWidgets.QLabel(self.detect_video_page)
        self.label_20.setGeometry(QtCore.QRect(20, 120, 911, 121))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("QLabel#label_20{\n"
"color: white;\n"
"}")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.errorvideo = QtWidgets.QLabel(self.detect_video_page)
        self.errorvideo.setGeometry(QtCore.QRect(290, 560, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.errorvideo.setFont(font)
        self.errorvideo.setStyleSheet("QLabel#errorvideo{\n"
"color: white;\n"
"}")
        self.errorvideo.setText("")
        self.errorvideo.setAlignment(QtCore.Qt.AlignCenter)
        self.errorvideo.setObjectName("errorvideo")
        self.fileLabel_2 = QtWidgets.QLabel(self.detect_video_page)
        self.fileLabel_2.setGeometry(QtCore.QRect(350, 332, 341, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe WP Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.fileLabel_2.setFont(font)
        self.fileLabel_2.setStyleSheet("QLabel#fileLabel_2{\n"
"color: white;\n"
"border-radius:4px;\n"
"  border: 2px solid white;\n"
"}")
        self.fileLabel_2.setObjectName("fileLabel_2")
        self.openFilebtn_2 = QtWidgets.QPushButton(self.detect_video_page)
        self.openFilebtn_2.setGeometry(QtCore.QRect(260, 330, 82, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe WP Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.openFilebtn_2.setFont(font)
        self.openFilebtn_2.setStyleSheet("QPushButton#openFilebtn_2{\n"
"    background-color: Transparent;\n"
"    background-repeat:no-repeat;\n"
"       border: 2px solid white;\n"
"    color: white;\n"
"border-radius:8px;\n"
"\n"
"}\n"
"QPushButton:hover#openFilebtn_2{\n"
"    background-color: white;\n"
"    border-color: white;\n"
"    color: black;\n"
"    border: 2px solid white;\n"
"border-radius: 8px;\n"
"}")
        self.openFilebtn_2.setObjectName("openFilebtn_2")
        self.stackedWidget_2.addWidget(self.detect_video_page)
        self.detect_webcam_page = QtWidgets.QWidget()
        self.detect_webcam_page.setObjectName("detect_webcam_page")
        self.label_10 = QtWidgets.QLabel(self.detect_webcam_page)
        self.label_10.setGeometry(QtCore.QRect(40, 40, 911, 121))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("QLabel#label_10{\n"
"color: white;\n"
"}")
        self.label_10.setObjectName("label_10")
        self.label_13 = QtWidgets.QLabel(self.detect_webcam_page)
        self.label_13.setGeometry(QtCore.QRect(340, 220, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe WP Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("QLabel#label_13{\n"
"color:white;\n"
"}")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.detect_webcam_page)
        self.label_14.setGeometry(QtCore.QRect(340, 300, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe WP Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("QLabel#label_14{\n"
"color:white;\n"
"}")
        self.label_14.setObjectName("label_14")
        self.detectCamera = QtWidgets.QPushButton(self.detect_webcam_page)
        self.detectCamera.setGeometry(QtCore.QRect(350, 410, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe WP Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.detectCamera.setFont(font)
        self.detectCamera.setStyleSheet("QPushButton#detectCamera{\n"
"    background-color: Transparent;\n"
"    background-repeat:no-repeat;\n"
"    border: 2px solid white;\n"
"    color: white;\n"
"border-radius:8px;\n"
"\n"
"}\n"
"QPushButton:hover#detectCamera{\n"
"    background-color: white;\n"
"    border-color: white;\n"
"    color: black;\n"
"border-radius: 8px;\n"
"    border: 2px solid white;\n"
"}")
        self.detectCamera.setObjectName("detectCamera")
        self.cameraerror = QtWidgets.QLabel(self.detect_webcam_page)
        self.cameraerror.setGeometry(QtCore.QRect(300, 380, 361, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cameraerror.setFont(font)
        self.cameraerror.setStyleSheet("QLabel#cameraerror{\n"
"color:red;\n"
"}")
        self.cameraerror.setText("")
        self.cameraerror.setAlignment(QtCore.Qt.AlignCenter)
        self.cameraerror.setObjectName("cameraerror")
        self.cameraIP = QtWidgets.QLineEdit(self.detect_webcam_page)
        self.cameraIP.setGeometry(QtCore.QRect(340, 250, 271, 31))
        self.cameraIP.setStyleSheet("QLineEdit#cameraIP\n"
"{\n"
"border-radius:8px;\n"
"padding-left: 5px;\n"
"}")
        self.cameraIP.setObjectName("cameraIP")
        self.locationCamera = QtWidgets.QLineEdit(self.detect_webcam_page)
        self.locationCamera.setGeometry(QtCore.QRect(340, 340, 271, 31))
        self.locationCamera.setStyleSheet("QLineEdit#locationCamera\n"
"{\n"
"border-radius:8px;\n"
"padding-left: 5px;\n"
"}")
        self.locationCamera.setObjectName("locationCamera")
        self.saveNotificationsImage_2 = QtWidgets.QCheckBox(self.detect_webcam_page)
        self.saveNotificationsImage_2.setGeometry(QtCore.QRect(350, 160, 241, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe WP Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.saveNotificationsImage_2.setFont(font)
        self.saveNotificationsImage_2.setStyleSheet("QCheckBox{\n"
"color: white;\n"
"}")
        self.saveNotificationsImage_2.setObjectName("saveNotificationsImage_2")
        self.label_9 = QtWidgets.QLabel(self.detect_webcam_page)
        self.label_9.setGeometry(QtCore.QRect(350, 460, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("QLabel#label_9{\n"
"color: white;\n"
"}")
        self.label_9.setText("")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.stackedWidget_2.addWidget(self.detect_webcam_page)
        self.stackedWidget.addWidget(self.first_page)
        self.login_page = QtWidgets.QWidget()
        self.login_page.setStyleSheet("QWidget#login_page{\n"
"background-color: #464646;\n"
"}")
        self.login_page.setObjectName("login_page")
        self.groupBox = QtWidgets.QGroupBox(self.login_page)
        self.groupBox.setGeometry(QtCore.QRect(190, 170, 861, 481))
        font = QtGui.QFont()
        font.setFamily("Modern")
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("QGroupBox{\n"
"background: #FFFFFF;\n"
"box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.2), 0 5px 5px 0 rgba(0, 0, 0, 0.24);\n"
" border-radius: 10px;\n"
"}")
        self.groupBox.setTitle("")
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.LoginButton = QtWidgets.QPushButton(self.groupBox)
        self.LoginButton.setGeometry(QtCore.QRect(510, 270, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe WP Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.LoginButton.setFont(font)
        self.LoginButton.setStyleSheet("QPushButton#LoginButton {\n"
"  background-color: #4CAF50;\n"
"  color: white;\n"
"  border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover#LoginButton {\n"
"  background-color: #60ba64;\n"
"}")
        self.LoginButton.setObjectName("LoginButton")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(510, 235, 31, 21))
        self.label_2.setStyleSheet("image: url(./images/padlock.png);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("./password/padlock.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(510, 195, 31, 21))
        self.label_3.setStyleSheet("QLabel{\n"
"image: url(./images/boy.png);\n"
"}")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("./images/boy.png"))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(510, 130, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe WP Semibold")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(510, 190, 221, 31))
        self.lineEdit.setStyleSheet("QLineEdit {\n"
" border: 2px solid gray;\n"
" border-radius: 10px;\n"
"padding-left: 25px;\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(510, 230, 221, 31))
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
" border: 2px solid gray;\n"
" border-radius: 10px;\n"
" padding-left: 25px;\n"
"}\n"
"")
        self.lineEdit_2.setMaxLength(16)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_17 = QtWidgets.QLabel(self.groupBox)
        self.label_17.setGeometry(QtCore.QRect(510, 320, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe WP Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("QLabel#label_17{\n"
"    color: red;\n"
"}")
        self.label_17.setText("")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.groupBox)
        self.label_18.setGeometry(QtCore.QRect(90, 90, 261, 341))
        self.label_18.setText("")
        self.label_18.setPixmap(QtGui.QPixmap("./images/detection.png"))
        self.label_18.setObjectName("label_18")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(110, 50, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe WP Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setGeometry(QtCore.QRect(400, 40, 20, 391))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.signbtn = QtWidgets.QPushButton(self.groupBox)
        self.signbtn.setGeometry(QtCore.QRect(510, 440, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(True)
        self.signbtn.setFont(font)
        self.signbtn.setStyleSheet("QPushButton#signbtn{\n"
"background-color: Transparent;background-repeat:no-repeat;\n"
"color: #A0A0A0;\n"
"\n"
"}\n"
"QPushButton:hover#signbtn{\n"
" color: blue;\n"
"}")
        self.signbtn.setObjectName("signbtn")
        self.LoginButton.raise_()
        self.label_4.raise_()
        self.lineEdit.raise_()
        self.label_17.raise_()
        self.lineEdit_2.raise_()
        self.label_2.raise_()
        self.label_18.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.line.raise_()
        self.signbtn.raise_()
        self.stackedWidget.addWidget(self.login_page)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setStyleSheet("QWidget#page_3{\n"
"background-color: #464646;\n"
"}")
        self.page_3.setObjectName("page_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.page_3)
        self.groupBox_2.setGeometry(QtCore.QRect(200, 170, 861, 481))
        font = QtGui.QFont()
        font.setFamily("Modern")
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("QGroupBox{\n"
"background: #FFFFFF;\n"
"box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.2), 0 5px 5px 0 rgba(0, 0, 0, 0.24);\n"
" border-radius: 10px;\n"
"}")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.createAccountbtn = QtWidgets.QPushButton(self.groupBox_2)
        self.createAccountbtn.setGeometry(QtCore.QRect(580, 430, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe WP Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.createAccountbtn.setFont(font)
        self.createAccountbtn.setStyleSheet("QPushButton#createAccountbtn {\n"
"  background-color: #4CAF50;\n"
"  color: white;\n"
"  border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover#createAccountbtn {\n"
"  background-color: #60ba64;\n"
"}")
        self.createAccountbtn.setObjectName("createAccountbtn")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(320, 320, 31, 21))
        self.label_8.setStyleSheet("image: url(./images/padlock.png);")
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("./password/padlock.png"))
        self.label_8.setObjectName("label_8")
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        self.label_15.setGeometry(QtCore.QRect(320, 280, 31, 21))
        self.label_15.setStyleSheet("QLabel{\n"
"image: url(./images/boy.png);\n"
"}")
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap("./images/boy.png"))
        self.label_15.setObjectName("label_15")
        self.label_19 = QtWidgets.QLabel(self.groupBox_2)
        self.label_19.setGeometry(QtCore.QRect(300, 60, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe WP Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.usernamelabel = QtWidgets.QLineEdit(self.groupBox_2)
        self.usernamelabel.setGeometry(QtCore.QRect(320, 276, 221, 31))
        self.usernamelabel.setStyleSheet("QLineEdit {\n"
" border: 2px solid gray;\n"
" border-radius: 10px;\n"
"padding-left: 25px;\n"
"}")
        self.usernamelabel.setObjectName("usernamelabel")
        self.passwordlabel = QtWidgets.QLineEdit(self.groupBox_2)
        self.passwordlabel.setGeometry(QtCore.QRect(320, 316, 221, 31))
        self.passwordlabel.setStyleSheet("QLineEdit {\n"
" border: 2px solid gray;\n"
" border-radius: 10px;\n"
" padding-left: 25px;\n"
"}\n"
"")
        self.passwordlabel.setMaxLength(16)
        self.passwordlabel.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordlabel.setObjectName("passwordlabel")
        self.label_23 = QtWidgets.QLabel(self.groupBox_2)
        self.label_23.setGeometry(QtCore.QRect(30, 100, 261, 351))
        self.label_23.setText("")
        self.label_23.setPixmap(QtGui.QPixmap("./images/detection.png"))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.groupBox_2)
        self.label_24.setGeometry(QtCore.QRect(30, 50, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe WP Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.line_7 = QtWidgets.QFrame(self.groupBox_2)
        self.line_7.setGeometry(QtCore.QRect(280, 50, 20, 391))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.passwordlabel2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.passwordlabel2.setGeometry(QtCore.QRect(320, 356, 221, 31))
        self.passwordlabel2.setStyleSheet("QLineEdit {\n"
" border: 2px solid gray;\n"
" border-radius: 10px;\n"
" padding-left: 25px;\n"
"}\n"
"")
        self.passwordlabel2.setMaxLength(16)
        self.passwordlabel2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordlabel2.setObjectName("passwordlabel2")
        self.firstnamelabel = QtWidgets.QLineEdit(self.groupBox_2)
        self.firstnamelabel.setGeometry(QtCore.QRect(320, 110, 221, 31))
        self.firstnamelabel.setStyleSheet("QLineEdit {\n"
" border: 2px solid gray;\n"
" border-radius: 10px;\n"
" padding-left: 25px;\n"
"}\n"
"")
        self.firstnamelabel.setMaxLength(16)
        self.firstnamelabel.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.firstnamelabel.setObjectName("firstnamelabel")
        self.surnamelabel = QtWidgets.QLineEdit(self.groupBox_2)
        self.surnamelabel.setGeometry(QtCore.QRect(320, 150, 221, 31))
        self.surnamelabel.setStyleSheet("QLineEdit {\n"
" border: 2px solid gray;\n"
" border-radius: 10px;\n"
" padding-left: 25px;\n"
"}\n"
"")
        self.surnamelabel.setMaxLength(16)
        self.surnamelabel.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.surnamelabel.setObjectName("surnamelabel")
        self.emaillabel = QtWidgets.QLineEdit(self.groupBox_2)
        self.emaillabel.setGeometry(QtCore.QRect(320, 190, 221, 31))
        self.emaillabel.setStyleSheet("QLineEdit {\n"
" border: 2px solid gray;\n"
" border-radius: 10px;\n"
" padding-left: 25px;\n"
"}\n"
"")
        self.emaillabel.setMaxLength(30)
        self.emaillabel.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.emaillabel.setObjectName("emaillabel")
        self.label_25 = QtWidgets.QLabel(self.groupBox_2)
        self.label_25.setGeometry(QtCore.QRect(320, 360, 31, 21))
        self.label_25.setStyleSheet("image: url(./images/padlock.png);")
        self.label_25.setText("")
        self.label_25.setPixmap(QtGui.QPixmap("./password/padlock.png"))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.groupBox_2)
        self.label_26.setGeometry(QtCore.QRect(290, 230, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe WP Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.groupBox_2)
        self.label_27.setGeometry(QtCore.QRect(470, 10, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe WP Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.passwordBtn = QtWidgets.QPushButton(self.groupBox_2)
        self.passwordBtn.setGeometry(QtCore.QRect(590, 224, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe WP Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.passwordBtn.setFont(font)
        self.passwordBtn.setStyleSheet("QPushButton#passwordBtn\n"
"{\n"
"background-color: Transparent;background-repeat:no-repeat;\n"
"\n"
"Text-align:left;\n"
"}\n"
"")
        self.passwordBtn.setObjectName("passwordBtn")
        self.usernameBtn = QtWidgets.QPushButton(self.groupBox_2)
        self.usernameBtn.setGeometry(QtCore.QRect(590, 184, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.usernameBtn.setFont(font)
        self.usernameBtn.setStyleSheet("QPushButton#usernameBtn\n"
"{\n"
"background-color: Transparent;background-repeat:no-repeat;\n"
"\n"
"Text-align:left;\n"
"}\n"
"")
        self.usernameBtn.setObjectName("usernameBtn")
        self.emailBtn = QtWidgets.QPushButton(self.groupBox_2)
        self.emailBtn.setGeometry(QtCore.QRect(590, 144, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.emailBtn.setFont(font)
        self.emailBtn.setStyleSheet("QPushButton#emailBtn{\n"
"background-color: Transparent;background-repeat:no-repeat;\n"
"\n"
"Text-align:left;\n"
"}\n"
"")
        self.emailBtn.setObjectName("emailBtn")
        self.emailImg = QtWidgets.QLabel(self.groupBox_2)
        self.emailImg.setGeometry(QtCore.QRect(565, 150, 21, 21))
        self.emailImg.setText("")
        self.emailImg.setPixmap(QtGui.QPixmap("./images/wrongcross.png"))
        self.emailImg.setScaledContents(True)
        self.emailImg.setObjectName("emailImg")
        self.passwordImg = QtWidgets.QLabel(self.groupBox_2)
        self.passwordImg.setGeometry(QtCore.QRect(565, 230, 21, 21))
        self.passwordImg.setText("")
        self.passwordImg.setPixmap(QtGui.QPixmap("./images/wrongcross.png"))
        self.passwordImg.setScaledContents(True)
        self.passwordImg.setObjectName("passwordImg")
        self.UsernameImg = QtWidgets.QLabel(self.groupBox_2)
        self.UsernameImg.setGeometry(QtCore.QRect(565, 190, 21, 21))
        self.UsernameImg.setText("")
        self.UsernameImg.setPixmap(QtGui.QPixmap("./images/wrongcross.png"))
        self.UsernameImg.setScaledContents(True)
        self.UsernameImg.setObjectName("UsernameImg")
        self.passwordBtn_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.passwordBtn_2.setGeometry(QtCore.QRect(590, 264, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.passwordBtn_2.setFont(font)
        self.passwordBtn_2.setStyleSheet("QPushButton#passwordBtn_2\n"
"{\n"
"background-color: Transparent;background-repeat:no-repeat;\n"
"\n"
"Text-align:left;\n"
"}\n"
"")
        self.passwordBtn_2.setObjectName("passwordBtn_2")
        self.passwordImg_2 = QtWidgets.QLabel(self.groupBox_2)
        self.passwordImg_2.setGeometry(QtCore.QRect(565, 270, 21, 21))
        self.passwordImg_2.setText("")
        self.passwordImg_2.setPixmap(QtGui.QPixmap("./images/wrongcross.png"))
        self.passwordImg_2.setScaledContents(True)
        self.passwordImg_2.setObjectName("passwordImg_2")
        self.passwordImg_3 = QtWidgets.QLabel(self.groupBox_2)
        self.passwordImg_3.setGeometry(QtCore.QRect(565, 306, 21, 21))
        self.passwordImg_3.setText("")
        self.passwordImg_3.setPixmap(QtGui.QPixmap("./images/wrongcross.png"))
        self.passwordImg_3.setScaledContents(True)
        self.passwordImg_3.setObjectName("passwordImg_3")
        self.passwordBtn_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.passwordBtn_3.setGeometry(QtCore.QRect(590, 300, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.passwordBtn_3.setFont(font)
        self.passwordBtn_3.setStyleSheet("QPushButton#passwordBtn_3\n"
"{\n"
"background-color: Transparent;background-repeat:no-repeat;\n"
"\n"
"Text-align:left;\n"
"}\n"
"")
        self.passwordBtn_3.setObjectName("passwordBtn_3")
        self.passwordImg_4 = QtWidgets.QLabel(self.groupBox_2)
        self.passwordImg_4.setGeometry(QtCore.QRect(565, 340, 21, 21))
        self.passwordImg_4.setText("")
        self.passwordImg_4.setPixmap(QtGui.QPixmap("./images/wrongcross.png"))
        self.passwordImg_4.setScaledContents(True)
        self.passwordImg_4.setObjectName("passwordImg_4")
        self.passwordBtn_4 = QtWidgets.QPushButton(self.groupBox_2)
        self.passwordBtn_4.setGeometry(QtCore.QRect(590, 334, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe WP Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.passwordBtn_4.setFont(font)
        self.passwordBtn_4.setStyleSheet("QPushButton#passwordBtn_4\n"
"{\n"
"background-color: Transparent;background-repeat:no-repeat;\n"
"\n"
"Text-align:left;\n"
"}\n"
"")
        self.passwordBtn_4.setObjectName("passwordBtn_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(570, 110, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.createAccountbtn.raise_()
        self.label_19.raise_()
        self.usernamelabel.raise_()
        self.passwordlabel.raise_()
        self.label_23.raise_()
        self.label_24.raise_()
        self.line_7.raise_()
        self.passwordlabel2.raise_()
        self.firstnamelabel.raise_()
        self.surnamelabel.raise_()
        self.emaillabel.raise_()
        self.label_15.raise_()
        self.label_8.raise_()
        self.label_25.raise_()
        self.label_26.raise_()
        self.label_27.raise_()
        self.passwordBtn.raise_()
        self.usernameBtn.raise_()
        self.emailBtn.raise_()
        self.emailImg.raise_()
        self.passwordImg.raise_()
        self.UsernameImg.raise_()
        self.passwordBtn_2.raise_()
        self.passwordImg_2.raise_()
        self.passwordImg_3.raise_()
        self.passwordBtn_3.raise_()
        self.passwordImg_4.raise_()
        self.passwordBtn_4.raise_()
        self.label_5.raise_()
        self.stackedWidget.addWidget(self.page_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget_4.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(3)
        self.stackedWidget_3.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Smoke detector"))
        self.usernotifications.setText(_translate("MainWindow", "   Notifications"))
        self.webcamDetect.setText(_translate("MainWindow", "   Detect webcam"))
        self.detectimage.setText(_translate("MainWindow", "   Detect Image"))
        self.detectvideo.setText(_translate("MainWindow", "   Detect video"))
        self.userSettings.setText(_translate("MainWindow", "   Settings"))
        self.logout.setText(_translate("MainWindow", "  Logout"))
        self.smokeTitle.setText(_translate("MainWindow", "  Smoke detector"))
        self.label_34.setText(_translate("MainWindow", "Notification filter"))
        self.label_35.setText(_translate("MainWindow", "Detection filter: "))
        self.checkBox.setText(_translate("MainWindow", "Image"))
        self.checkBox_2.setText(_translate("MainWindow", "Video"))
        self.checkBox_3.setText(_translate("MainWindow", "Webcam"))
        self.label_36.setText(_translate("MainWindow", "Date filter: "))
        self.label_37.setText(_translate("MainWindow", "to"))
        self.filterbtn.setText(_translate("MainWindow", "Filter"))
        self.label_38.setText(_translate("MainWindow", "For one date filter leave any as default"))
        self.homebutton.setText(_translate("MainWindow", "   Home"))
        self.changeUserInfobtn.setText(_translate("MainWindow", "Change user info"))
        self.Changepasswordbtn.setText(_translate("MainWindow", "Change password"))
        self.label_28.setText(_translate("MainWindow", "Email:"))
        self.label_16.setText(_translate("MainWindow", "First name:"))
        self.label_22.setText(_translate("MainWindow", "Surname:"))
        self.saveuserinfobtn.setText(_translate("MainWindow", "save user info"))
        self.label_29.setText(_translate("MainWindow", "Current password"))
        self.label_30.setText(_translate("MainWindow", "New password"))
        self.label_31.setText(_translate("MainWindow", "re-enter new password"))
        self.savenewpasswordbtn.setText(_translate("MainWindow", "save new password"))
        self.label_7.setText(_translate("MainWindow", "Notifications"))
        self.backToNotification.setText(_translate("MainWindow", "     Back"))
        self.label_39.setText(_translate("MainWindow", "Home"))
        self.label_41.setText(_translate("MainWindow", "Information about the application:"))
        self.label_42.setText(_translate("MainWindow", "• The application provides user with the automatic detection of smokers within a given location. "))
        self.label_43.setText(_translate("MainWindow", "• Due the processing power required, adequate features might not be avaliable or function as implemented on commondity PCs."))
        self.label_44.setText(_translate("MainWindow", "• This is application is intended for industry use or the prevention of smoking in strictly prohibited areas, such as schools. "))
        self.label_45.setText(_translate("MainWindow", "• Due to the high requiring processing power, the use of the application requires NVIDIA graphics card in order to function flawlessly. "))
        self.label_47.setText(_translate("MainWindow", "Features provided:"))
        self.label_48.setText(_translate("MainWindow", "• Automatic detection of smokers within a uploaded live webcam from the user. "))
        self.label_49.setText(_translate("MainWindow", "• Automatic detection of smokers within a uploaded video from the user."))
        self.label_50.setText(_translate("MainWindow", "• Automatic detection of smokers within a uploaded image from the user."))
        self.label_51.setText(_translate("MainWindow", "• Every 30 seconds a screenshot is taken for a uploaded video/webcam if it detects a smoker."))
        self.label_52.setText(_translate("MainWindow", "• Screenshots of detected smokers are saved in notifications and illustrates, the date, time and type of detection. "))
        self.label_53.setText(_translate("MainWindow", "• Screenshots are also saved in the users local folders. "))
        self.label_54.setText(_translate("MainWindow", "• Screenshots can be enlarged, saved and deleted in the notificiation page."))
        self.openFilebtn.setText(_translate("MainWindow", "Open file"))
        self.imagedetectbtn.setText(_translate("MainWindow", "Detect"))
        self.label_11.setText(_translate("MainWindow", "Upload image"))
        self.label_12.setText(_translate("MainWindow", "Upload any image .jpg, .png etc and set a path to where you wish the image to be loaded"))
        self.setPathbtn.setText(_translate("MainWindow", "Set path"))
        self.fileLabel.setText(_translate("MainWindow", "Open file path"))
        self.pathLabel.setText(_translate("MainWindow", "set file path"))
        self.saveNotificationsImage.setText(_translate("MainWindow", "Save in notifications"))
        self.saveNotificationsImage_3.setText(_translate("MainWindow", "Save detections in notifications"))
        self.detectCamera_2.setText(_translate("MainWindow", "Detect video"))
        self.label_20.setText(_translate("MainWindow", "Add the video path in order to start detected smokers within a video, detections will be saved in videoimages folder"))
        self.fileLabel_2.setText(_translate("MainWindow", "Open file path"))
        self.openFilebtn_2.setText(_translate("MainWindow", "Open file"))
        self.label_10.setText(_translate("MainWindow", "Type in the camera IP to open up a new window that will detect at that location. If you wish to detect through webcam the IP is 0."))
        self.label_13.setText(_translate("MainWindow", "Camera IP:"))
        self.label_14.setText(_translate("MainWindow", "Location:"))
        self.detectCamera.setText(_translate("MainWindow", "Detect camera"))
        self.saveNotificationsImage_2.setText(_translate("MainWindow", "Save detections in notifications"))
        self.LoginButton.setText(_translate("MainWindow", "LOGIN"))
        self.label_4.setText(_translate("MainWindow", "Member Login"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Username"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Password"))
        self.label.setText(_translate("MainWindow", "Detect smokers"))
        self.signbtn.setText(_translate("MainWindow", "Not a member? Sign up now"))
        self.createAccountbtn.setText(_translate("MainWindow", "Create account"))
        self.label_19.setText(_translate("MainWindow", "User info"))
        self.usernamelabel.setPlaceholderText(_translate("MainWindow", "Username"))
        self.passwordlabel.setPlaceholderText(_translate("MainWindow", "Password"))
        self.label_24.setText(_translate("MainWindow", "Detect smokers"))
        self.passwordlabel2.setPlaceholderText(_translate("MainWindow", "Re-enter password"))
        self.firstnamelabel.setPlaceholderText(_translate("MainWindow", "First name"))
        self.surnamelabel.setPlaceholderText(_translate("MainWindow", "Surname"))
        self.emaillabel.setPlaceholderText(_translate("MainWindow", "Email"))
        self.label_26.setText(_translate("MainWindow", "User login"))
        self.label_27.setText(_translate("MainWindow", "Member signup"))
        self.passwordBtn.setText(_translate("MainWindow", "Password must be longer than 4 characters"))
        self.usernameBtn.setText(_translate("MainWindow", "Username must be unique"))
        self.emailBtn.setText(_translate("MainWindow", "Email must be valid"))
        self.passwordBtn_2.setText(_translate("MainWindow", "Password must have a capital letter"))
        self.passwordBtn_3.setText(_translate("MainWindow", "Password must have a number"))
        self.passwordBtn_4.setText(_translate("MainWindow", "Passwords must be the same"))
        self.label_5.setText(_translate("MainWindow", "Steps:"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
