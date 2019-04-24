# -*- coding: utf-8 -*-

# self implementation generated from reading ui file 'customWidget.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class test_widget(QtWidgets.QWidget):
    def __init__ (self, parent = None):
        super(test_widget, self).__init__(parent)
        self.setFixedSize(274, 288)
        self.setStyleSheet("QWidget{\n"
"padding-left: 5px;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.customWidgetImage = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.customWidgetImage.sizePolicy().hasHeightForWidth())
        self.customWidgetImage.setSizePolicy(sizePolicy)
        self.customWidgetImage.setMinimumSize(QtCore.QSize(20, 30))
        self.customWidgetImage.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.customWidgetImage.setObjectName("customWidgetImage")
        self.verticalLayout.addWidget(self.customWidgetImage)
        self.customWidgetType = QtWidgets.QLabel(self)
        self.customWidgetType.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe WP Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.customWidgetType.setFont(font)
        self.customWidgetType.setStyleSheet("QLabel#customWidgetType{\n"
        "color: white;\n"
        "}")
        self.customWidgetType.setObjectName("customWidgetType")
        self.verticalLayout.addWidget(self.customWidgetType)
        self.customWidgetDate = QtWidgets.QLabel(self)
        self.customWidgetDate.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe WP Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.customWidgetDate.setFont(font)
        self.customWidgetDate.setStyleSheet("QLabel#customWidgetDate{\n"
        "color: white;\n"
        "}")
        self.customWidgetDate.setObjectName("customWidgetDate")
        self.verticalLayout.addWidget(self.customWidgetDate)
        self.customWidgetScore = QtWidgets.QLabel(self)
        self.customWidgetScore.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe WP Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.customWidgetScore.setFont(font)
        self.customWidgetScore.setStyleSheet("QLabel#customWidgetScore{\n"
        "color: white;\n"
        "}")
        self.customWidgetScore.setObjectName("customWidgetScore")
        self.verticalLayout.addWidget(self.customWidgetScore)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.customWidgetImage.setText("Image")
        self.customWidgetType.setText("Type")
        self.customWidgetDate.setText("Date")
        self.customWidgetScore.setText("Time")



    def setLabelDate(self,text):
        self.customWidgetDate.setText(text)
    def setLabelTime(self,text):
        self.customWidgetScore.setText(text)
    def setLabelType(self,text):
        self.customWidgetType.setText(text)
    def setImage(self, text):
        pixmap1 = QtGui.QPixmap()
        pixmap1.loadFromData(text)
        pixmap = QtGui.QPixmap(pixmap1)
        scaled_pixmap = pixmap.scaled(200,200)
        self.customWidgetImage.setPixmap(QtGui.QPixmap(scaled_pixmap))

    def setImage1(self, text):
        pixmap = QtGui.QPixmap(text)
        scaled_pixmap = pixmap.scaled(200,200)
        self.customWidgetImage.setPixmap(QtGui.QPixmap(scaled_pixmap))
