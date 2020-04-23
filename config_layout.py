# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'config_layout.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.browser_area = QtWidgets.QScrollArea(self.centralwidget)
        self.browser_area.setGeometry(QtCore.QRect(440, 30, 320, 240))
        self.browser_area.setWidgetResizable(True)
        self.browser_area.setObjectName("browser_area")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 318, 238))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.browser_area.setWidget(self.scrollAreaWidgetContents)
        self.button_next = QtWidgets.QPushButton(self.centralwidget)
        self.button_next.setGeometry(QtCore.QRect(530, 320, 75, 23))
        self.button_next.setObjectName("button_next")
        self.button_Previous = QtWidgets.QPushButton(self.centralwidget)
        self.button_Previous.setGeometry(QtCore.QRect(450, 320, 75, 23))
        self.button_Previous.setObjectName("button_Previous")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(450, 290, 91, 16))
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(450, 310, 118, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 411, 161))
        self.label_2.setObjectName("label_2")
        self.button_setConfig = QtWidgets.QPushButton(self.centralwidget)
        self.button_setConfig.setGeometry(QtCore.QRect(610, 320, 75, 23))
        self.button_setConfig.setObjectName("button_setConfig")
        self.button_addPoint = QtWidgets.QPushButton(self.centralwidget)
        self.button_addPoint.setGeometry(QtCore.QRect(450, 390, 75, 23))
        self.button_addPoint.setObjectName("button_addPoint")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(450, 380, 118, 3))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(450, 360, 91, 16))
        self.label_3.setObjectName("label_3")
        self.button_done = QtWidgets.QPushButton(self.centralwidget)
        self.button_done.setGeometry(QtCore.QRect(690, 530, 75, 23))
        self.button_done.setObjectName("button_done")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(290, 40, 121, 101))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Camera Configuration"))
        self.button_next.setText(_translate("MainWindow", "Next"))
        self.button_Previous.setText(_translate("MainWindow", "Previous"))
        self.label.setText(_translate("MainWindow", "Camera Config"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">What Should I do?</span></p><p><span style=\" font-size:12pt;\">1. choose the most accurate target<br/>(Use the buttons to navigate)</span></p><p><span style=\" font-size:12pt;\">2. press set</span></p><p><span style=\" font-size:12pt;\">3. travel accrost the field, <br/>each time you see that target acquired, press &quot;add point&quot;</span></p><p><br/></p></body></html>"))
        self.button_setConfig.setText(_translate("MainWindow", "Set Config"))
        self.button_addPoint.setText(_translate("MainWindow", "Add Point"))
        self.label_3.setText(_translate("MainWindow", "Targets acquired"))
        self.button_done.setText(_translate("MainWindow", "Done!"))
