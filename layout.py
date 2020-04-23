# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(840, 736)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.Tabs.setGeometry(QtCore.QRect(20, 70, 781, 591))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.Tabs.setFont(font)
        self.Tabs.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Tabs.setObjectName("Tabs")
        self.control = QtWidgets.QWidget()
        self.control.setObjectName("control")
        self.layoutWidget = QtWidgets.QWidget(self.control)
        self.layoutWidget.setGeometry(QtCore.QRect(31, 48, 511, 30))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.entry_change_dns = QtWidgets.QLineEdit(self.layoutWidget)
        self.entry_change_dns.setObjectName("entry_change_dns")
        self.horizontalLayout_2.addWidget(self.entry_change_dns)
        self.button_change_dns = QtWidgets.QPushButton(self.layoutWidget)
        self.button_change_dns.setObjectName("button_change_dns")
        self.horizontalLayout_2.addWidget(self.button_change_dns)
        self.button_set_dhcp = QtWidgets.QPushButton(self.control)
        self.button_set_dhcp.setGeometry(QtCore.QRect(31, 85, 511, 28))
        self.button_set_dhcp.setObjectName("button_set_dhcp")
        self.label_control_logger = QtWidgets.QLabel(self.control)
        self.label_control_logger.setGeometry(QtCore.QRect(31, 187, 511, 31))
        self.label_control_logger.setText("")
        self.label_control_logger.setObjectName("label_control_logger")
        self.button_update_software = QtWidgets.QPushButton(self.control)
        self.button_update_software.setGeometry(QtCore.QRect(31, 225, 511, 28))
        self.button_update_software.setObjectName("button_update_software")
        self.button_reboot = QtWidgets.QPushButton(self.control)
        self.button_reboot.setGeometry(QtCore.QRect(31, 260, 511, 28))
        self.button_reboot.setObjectName("button_reboot")
        self.layoutWidget1 = QtWidgets.QWidget(self.control)
        self.layoutWidget1.setGeometry(QtCore.QRect(31, 120, 511, 30))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.entry_password1 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.entry_password1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.entry_password1.setObjectName("entry_password1")
        self.horizontalLayout_3.addWidget(self.entry_password1)
        self.entry_password2 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.entry_password2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.entry_password2.setObjectName("entry_password2")
        self.horizontalLayout_3.addWidget(self.entry_password2)
        self.change_password = QtWidgets.QPushButton(self.layoutWidget1)
        self.change_password.setObjectName("change_password")
        self.horizontalLayout_3.addWidget(self.change_password)
        self.layoutWidget2 = QtWidgets.QWidget(self.control)
        self.layoutWidget2.setGeometry(QtCore.QRect(31, 11, 511, 30))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.entry_set_ip = QtWidgets.QLineEdit(self.layoutWidget2)
        self.entry_set_ip.setObjectName("entry_set_ip")
        self.horizontalLayout.addWidget(self.entry_set_ip)
        self.button_set_ip = QtWidgets.QPushButton(self.layoutWidget2)
        self.button_set_ip.setObjectName("button_set_ip")
        self.horizontalLayout.addWidget(self.button_set_ip)
        self.Tabs.addTab(self.control, "")
        self.settings = QtWidgets.QWidget()
        self.settings.setObjectName("settings")
        self.label_2 = QtWidgets.QLabel(self.settings)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 55, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.settings)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 55, 16))
        self.label_3.setObjectName("label_3")
        self.layoutWidget3 = QtWidgets.QWidget(self.settings)
        self.layoutWidget3.setGeometry(QtCore.QRect(101, 21, 541, 256))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.combobox_choose_script = QtWidgets.QComboBox(self.layoutWidget3)
        self.combobox_choose_script.setObjectName("combobox_choose_script")
        self.verticalLayout_2.addWidget(self.combobox_choose_script)
        self.combobox_choose_grip = QtWidgets.QComboBox(self.layoutWidget3)
        self.combobox_choose_grip.setObjectName("combobox_choose_grip")
        self.verticalLayout_2.addWidget(self.combobox_choose_grip)
        self.entry_pipeline = QtWidgets.QLineEdit(self.layoutWidget3)
        self.entry_pipeline.setObjectName("entry_pipeline")
        self.verticalLayout_2.addWidget(self.entry_pipeline)
        self.entry_team_number = QtWidgets.QLineEdit(self.layoutWidget3)
        self.entry_team_number.setObjectName("entry_team_number")
        self.verticalLayout_2.addWidget(self.entry_team_number)
        self.entry_width = QtWidgets.QLineEdit(self.layoutWidget3)
        self.entry_width.setObjectName("entry_width")
        self.verticalLayout_2.addWidget(self.entry_width)
        self.entry_height = QtWidgets.QLineEdit(self.layoutWidget3)
        self.entry_height.setObjectName("entry_height")
        self.verticalLayout_2.addWidget(self.entry_height)
        self.entry_fps = QtWidgets.QLineEdit(self.layoutWidget3)
        self.entry_fps.setObjectName("entry_fps")
        self.verticalLayout_2.addWidget(self.entry_fps)
        self.label_settings_logger = QtWidgets.QLabel(self.layoutWidget3)
        self.label_settings_logger.setText("")
        self.label_settings_logger.setObjectName("label_settings_logger")
        self.verticalLayout_2.addWidget(self.label_settings_logger)
        self.button_save = QtWidgets.QPushButton(self.layoutWidget3)
        self.button_save.setObjectName("button_save")
        self.verticalLayout_2.addWidget(self.button_save)
        self.Tabs.addTab(self.settings, "")
        self.GRIP = QtWidgets.QWidget()
        self.GRIP.setObjectName("GRIP")
        self.layoutWidget_6 = QtWidgets.QWidget(self.GRIP)
        self.layoutWidget_6.setGeometry(QtCore.QRect(20, 60, 200, 121))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.layoutWidget_6)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_15 = QtWidgets.QLabel(self.layoutWidget_6)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_9.addWidget(self.label_15)
        self.combobox_fm_grips = QtWidgets.QComboBox(self.layoutWidget_6)
        self.combobox_fm_grips.setObjectName("combobox_fm_grips")
        self.verticalLayout_9.addWidget(self.combobox_fm_grips)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.button_push_grip = QtWidgets.QPushButton(self.layoutWidget_6)
        self.button_push_grip.setObjectName("button_push_grip")
        self.horizontalLayout_9.addWidget(self.button_push_grip)
        self.button_delete_grip = QtWidgets.QPushButton(self.layoutWidget_6)
        self.button_delete_grip.setObjectName("button_delete_grip")
        self.horizontalLayout_9.addWidget(self.button_delete_grip)
        self.verticalLayout_9.addLayout(self.horizontalLayout_9)
        self.label = QtWidgets.QLabel(self.GRIP)
        self.label.setGeometry(QtCore.QRect(250, 30, 81, 16))
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.GRIP)
        self.line.setGeometry(QtCore.QRect(240, 50, 118, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.tableWidget = QtWidgets.QTableWidget(self.GRIP)
        self.tableWidget.setGeometry(QtCore.QRect(240, 60, 221, 121))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.checkBox = QtWidgets.QCheckBox(self.GRIP)
        self.checkBox.setGeometry(QtCore.QRect(60, 30, 101, 17))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.start_config = QtWidgets.QCommandLinkButton(self.GRIP)
        self.start_config.setGeometry(QtCore.QRect(490, 30, 185, 41))
        self.start_config.setObjectName("start_config")
        self.Tabs.addTab(self.GRIP, "")
        self.console_4 = QtWidgets.QWidget()
        self.console_4.setObjectName("console_4")
        self.console = QtWidgets.QLabel(self.console_4)
        self.console.setGeometry(QtCore.QRect(10, 10, 731, 531))
        self.console.setText("")
        self.console.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.console.setObjectName("console")
        self.Tabs.addTab(self.console_4, "")
        self.file_manager = QtWidgets.QWidget()
        self.file_manager.setObjectName("file_manager")
        self.label_fm_logger = QtWidgets.QLabel(self.file_manager)
        self.label_fm_logger.setGeometry(QtCore.QRect(20, 180, 681, 41))
        self.label_fm_logger.setText("")
        self.label_fm_logger.setObjectName("label_fm_logger")
        self.layoutWidget4 = QtWidgets.QWidget(self.file_manager)
        self.layoutWidget4.setGeometry(QtCore.QRect(20, 40, 141, 111))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.entry_reset_camera = QtWidgets.QLineEdit(self.layoutWidget4)
        self.entry_reset_camera.setObjectName("entry_reset_camera")
        self.verticalLayout_3.addWidget(self.entry_reset_camera)
        self.button_reset_camera = QtWidgets.QPushButton(self.layoutWidget4)
        self.button_reset_camera.setObjectName("button_reset_camera")
        self.verticalLayout_3.addWidget(self.button_reset_camera)
        self.layoutWidget5 = QtWidgets.QWidget(self.file_manager)
        self.layoutWidget5.setGeometry(QtCore.QRect(230, 40, 197, 121))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget5)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget5)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.combobox_fm_scripts = QtWidgets.QComboBox(self.layoutWidget5)
        self.combobox_fm_scripts.setObjectName("combobox_fm_scripts")
        self.verticalLayout_4.addWidget(self.combobox_fm_scripts)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.button_push_script = QtWidgets.QPushButton(self.layoutWidget5)
        self.button_push_script.setObjectName("button_push_script")
        self.horizontalLayout_4.addWidget(self.button_push_script)
        self.button_delete_script = QtWidgets.QPushButton(self.layoutWidget5)
        self.button_delete_script.setObjectName("button_delete_script")
        self.horizontalLayout_4.addWidget(self.button_delete_script)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.Tabs.addTab(self.file_manager, "")
        self.camera_control = QtWidgets.QWidget()
        self.camera_control.setObjectName("camera_control")
        self.browser_area = QtWidgets.QScrollArea(self.camera_control)
        self.browser_area.setGeometry(QtCore.QRect(10, 60, 721, 461))
        self.browser_area.setWidgetResizable(True)
        self.browser_area.setObjectName("browser_area")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 719, 459))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.browser_area.setWidget(self.scrollAreaWidgetContents)
        self.layoutWidget6 = QtWidgets.QWidget(self.camera_control)
        self.layoutWidget6.setGeometry(QtCore.QRect(10, 10, 381, 31))
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.layoutWidget6)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.entry_camera_number = QtWidgets.QLineEdit(self.layoutWidget6)
        self.entry_camera_number.setObjectName("entry_camera_number")
        self.horizontalLayout_10.addWidget(self.entry_camera_number)
        self.button_refresh_browser = QtWidgets.QPushButton(self.layoutWidget6)
        self.button_refresh_browser.setObjectName("button_refresh_browser")
        self.horizontalLayout_10.addWidget(self.button_refresh_browser)
        self.button_calibrate_camera = QtWidgets.QPushButton(self.layoutWidget6)
        self.button_calibrate_camera.setObjectName("button_calibrate_camera")
        self.horizontalLayout_10.addWidget(self.button_calibrate_camera)
        self.Tabs.addTab(self.camera_control, "")
        self.entry_ssh = QtWidgets.QLineEdit(self.centralwidget)
        self.entry_ssh.setGeometry(QtCore.QRect(10, 10, 361, 22))
        self.entry_ssh.setObjectName("entry_ssh")
        self.entry_password = QtWidgets.QLineEdit(self.centralwidget)
        self.entry_password.setGeometry(QtCore.QRect(380, 10, 141, 22))
        self.entry_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.entry_password.setObjectName("entry_password")
        self.button_connect = QtWidgets.QPushButton(self.centralwidget)
        self.button_connect.setGeometry(QtCore.QRect(530, 10, 131, 28))
        self.button_connect.setObjectName("button_connect")
        self.Logo = QtWidgets.QLabel(self.centralwidget)
        self.Logo.setGeometry(QtCore.QRect(710, 10, 71, 71))
        self.Logo.setText("")
        self.Logo.setPixmap(QtGui.QPixmap(":/images/HawkEye.png"))
        self.Logo.setScaledContents(True)
        self.Logo.setObjectName("Logo")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 840, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Tabs.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hawk Controller"))
        self.entry_change_dns.setPlaceholderText(_translate("MainWindow", "new dns"))
        self.button_change_dns.setText(_translate("MainWindow", "change dns(root)"))
        self.button_set_dhcp.setText(_translate("MainWindow", "set dhcp(root)"))
        self.button_update_software.setText(_translate("MainWindow", "update software"))
        self.button_reboot.setText(_translate("MainWindow", "reboot microprocessor(log in as root)"))
        self.entry_password1.setPlaceholderText(_translate("MainWindow", "new password"))
        self.entry_password2.setPlaceholderText(_translate("MainWindow", "confirm"))
        self.change_password.setText(_translate("MainWindow", "change password"))
        self.entry_set_ip.setPlaceholderText(_translate("MainWindow", "recommended 10.TE.AM.11 (root only sets eth0)"))
        self.button_set_ip.setText(_translate("MainWindow", "set ip(root)"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.control), _translate("MainWindow", "control"))
        self.label_2.setText(_translate("MainWindow", "script file"))
        self.label_3.setText(_translate("MainWindow", "grip file"))
        self.entry_pipeline.setPlaceholderText(_translate("MainWindow", "pipeline name - vision"))
        self.entry_team_number.setPlaceholderText(_translate("MainWindow", "team number"))
        self.entry_width.setPlaceholderText(_translate("MainWindow", "width - 160"))
        self.entry_height.setPlaceholderText(_translate("MainWindow", "height - 120"))
        self.entry_fps.setPlaceholderText(_translate("MainWindow", "frames per second - 30"))
        self.button_save.setText(_translate("MainWindow", "save"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.settings), _translate("MainWindow", "settings"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p>grip manager<br/><span style=\" font-size:7pt;\">will work only if ML is disabled.</span></p></body></html>"))
        self.button_push_grip.setText(_translate("MainWindow", "push"))
        self.button_delete_grip.setText(_translate("MainWindow", "delete"))
        self.label.setText(_translate("MainWindow", "HSV Values:"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "H"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "S"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "V"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Min"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Max"))
        self.checkBox.setText(_translate("MainWindow", "ML Enabled"))
        self.start_config.setText(_translate("MainWindow", "Start Configuration"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.GRIP), _translate("MainWindow", "GRIP"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.console_4), _translate("MainWindow", "console"))
        self.label_6.setText(_translate("MainWindow", "camera configs"))
        self.entry_reset_camera.setPlaceholderText(_translate("MainWindow", "camera #"))
        self.button_reset_camera.setText(_translate("MainWindow", "reset"))
        self.label_7.setText(_translate("MainWindow", "script manager"))
        self.button_push_script.setText(_translate("MainWindow", "push"))
        self.button_delete_script.setText(_translate("MainWindow", "delete"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.file_manager), _translate("MainWindow", "file manager"))
        self.entry_camera_number.setPlaceholderText(_translate("MainWindow", "camera number"))
        self.button_refresh_browser.setText(_translate("MainWindow", "refresh"))
        self.button_calibrate_camera.setText(_translate("MainWindow", "calibrate"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.camera_control), _translate("MainWindow", "camera control"))
        self.entry_ssh.setPlaceholderText(_translate("MainWindow", "user@ip_address (defualt user root)"))
        self.entry_password.setPlaceholderText(_translate("MainWindow", "password"))
        self.button_connect.setText(_translate("MainWindow", "disconnected"))



#import src_rc