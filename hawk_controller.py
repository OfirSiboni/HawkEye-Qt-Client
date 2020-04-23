#!/usr/bin/python3

'''
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtGui import *
import sys
import paramiko
import json
import time
import os
import subprocess
class hawkController:

        REFRESH_RATE = 500
        PORT_ZERO = 1181
        path = os.path.dirname(os.path.abspath(__file__))
        hawk_controller = QApplication([])
        layout = uic.loadUi(path + "/ui/layout.ui")
        browser = QWebEngineView()
        browser.show()
        layout.browser_area.setWidget(browser)
        connected = False
        address = ''
        ssh_client = None


        def refresh():
                global ssh_client
                try:
                        if connected:
                                _, stdout, _ = ssh_client.exec_command("tail -n35 ~/.hawklog")
                                lines = stdout.read().decode('utf-8').splitlines()
                                lines = '\n'.join(lines)
                                layout.console.setText(lines)
                                timer.start(REFRESH_RATE)
                except Exception as e:
                        connection_lost('label_control_logger')
                        print(e)

        timer = QTimer()
        timer.timeout.connect(refresh)
        timer.setInterval(REFRESH_RATE)

        def get_label(name):
                return layout.findChild(QLabel, name)
            
        def get_combobox(name):
                return layout.findChild(QComboBox, name)

        def get_entry(name):
                return layout.findChild(QLineEdit, name)

        def connection_lost(logger_name):
                global ssh_client
                global connected
                global address
                ssh_client = None
                connected = False
                address = ''
                get_label(logger_name).setText("lost connection!")
                layout.button_connect.setText('disconnected')
                timer.stop()


        def populate_combo(combo, str_array):
                get_combobox(combo).clear()
                get_combobox(combo).addItems(str_array)

        def update_file_manager():
                try:
                        ls_scripts = ssh_client.exec_command("ls ~/.hawk/scripts")[1].read()
                        ls_grips = ssh_client.exec_command("ls ~/.hawk/grips")[1].read()
                        ls_scripts = ls_scripts.decode('utf-8').strip('\n').splitlines()
                        ls_grips = ls_grips.decode('utf-8').strip('\n').splitlines()
                        populate_combo('combobox_fm_scripts', ls_scripts)
                        populate_combo('combobox_choose_script', ls_scripts)
                        populate_combo('combobox_fm_grips', ls_grips)
                        populate_combo('combobox_choose_grip', ls_grips)
                except Exception as e:
                        connection_lost('label_fm_logger')
                        print(e)

        def delete_file(reletive_path):
                try:
                        ssh_client.exec_command("rm ~/.hawk/" + reletive_path)
                        get_label('label_fm_logger').setText('done')
                except Exception as e:
                        connection_lost('label_fm_logger')
                        print(e)

        def destroy(arg):
                Gtk.main_quit()

        def send_file(local_path, remote_path):
                global ssh_client
                if ssh_client != None:
                        try:
                                with open(local_path) as file:
                                        file_contant = "".join(i for i in file.readlines()).replace('"', '\\"').replace("'", "\'")
                                        ssh_client.exec_command('echo "' + file_contant + '" > ' + remote_path)
                                get_label('label_fm_logger').setText('')
                        except Exception as e:
                                get_label('label_fm_logger').setText(str(e))
                else:
                        get_label('label_fm_logger').setText("you are disconnected")

        def digits_only(entry_name):
                text = get_entry(entry_name).text().strip()
                get_entry(entry_name).setText(''.join([i for i in text if i in '0123456789']))

        def button_connect_clicked(arg):
                global connected
                global ssh_client
                global address
                try:
                        if not connected:
                                ssh_client = paramiko.SSHClient()
                                ssh_client.load_system_host_keys()
                                address = get_entry('entry_ssh').text()
                                username = address.split('@')[0]
                                hostname = address.split('@')[1]
                                address = hostname
                                password = get_entry('entry_password').text()
                                ssh_client.load_system_host_keys()
                                ssh_client.connect(hostname, username=username, password=password)
                                ssh_client.exec_command("mkdir ~/.hawk")
                                ssh_client.exec_command("mkdir ~/.hawk/grips")
                                ssh_client.exec_command("mkdir ~/.hawk/scripts")
                                ssh_client.exec_command("mkdir ~/.hawk/cameras")
                                connected = True
                                layout.button_connect.setText('connected')
                                get_label('label_control_logger').setText('')
                                update_file_manager()
                                globals.ssh_Client = ssh_client
                                layout.console.setText('')
                                layout.entry_camera_number.setText('0')
                                refresh()
                        else:
                                ssh_client = None
                                connected = False
                                layout.button_connect.setText('disconnected')
                                get_label('label_control_logger').setText('')
                                get_label('label_settings_logger').setText('')
                                get_label('label_fm_logger').setText('')
                                populate_combo('combobox_fm_scripts', [])
                                populate_combo('combobox_fm_grips', [])
                                populate_combo('combobox_choose_script', [])
                                populate_combo('combobox_choose_grip', [])
                                timer.stop()
                except Exception as e:
                        get_label('label_control_logger').setText('cannot connect')
                        connected = False
                        ssh_client = None
                        layout.button_connect.setText('disconnected')
                        timer.stop()
                        print(e)

        def button_change_password_clicked(arg):
                try:
                        password1 = get_entry('entry_password1').text()
                        password2 = get_entry('entry_password2').text()
                        if password1 == password2:
                                ssh_client.exec_command("~/hawk-vision/scripts/change_password.sh " + password1)
                                get_label('label_control_logger').setText("password changed")
                        else:
                                get_label('label_control_logger').setText("passwords don't match")
                except Exception as e:
                        connection_lost('label_control_logger')
                        print(e)
        port = 1181
        def entry_camera_number_changed(arg):
                global address
                digits_only('entry_camera_number')
                port = str(int(get_entry('entry_camera_number').text()) + PORT_ZERO)
                url = 'http://' + address + ':' + port
                browser.load(QUrl(url))
                
        def button_calibrate_camera_clicked(arg):
                try:
                        port = get_entry('entry_camera_number').text()
                        ssh_client.exec_command('~/hawk-vision/scripts/config_camera.sh ' + port)
                except Exception as e:
                        connection_lost('label_control_logger')
                        print(e)

        def button_refresh_camera_clicked(arg):
                browser.reload()

        def button_reboot_clicked(arg):
                global ssh_client
                try:
                        ssh_client.exec_command("reboot")
                except Exception as e:
                        connection_lost('label_control_logger')
                        print(e)

        def entry_team_number_changed(arg):
                digits_only('entry_team_number')

        def entry_width_changed(arg):
                digits_only('entry_width')

        def entry_height_changed(arg):
                digits_only('entry_height')

        def entry_fps_changed(arg):
                digits_only('entry_fps')

        def button_save_clicked(arg):
                global ssh_client
                try:
                        script_file = get_combobox('combobox_choose_script').currentText().strip() or ''
                        grip_file = get_combobox('combobox_choose_grip').currentText().strip() or ''
                        pipeline_name = (get_entry('entry_pipeline').text()) or 'vision'
                        team_number = (get_entry('entry_team_number').text()) or -1
                        width = get_entry('entry_width').text() or 160
                        height = get_entry('entry_height').text() or 120
                        fps = get_entry('entry_fps').text() or 30
                        if team_number == -1:
                                get_label('label_settings_logger').setText('please select team number')
                                return
                        if script_file == '' or grip_file == '':
                                get_label('label_settings_logger').setText('please select grip file and script file')
                                return
                        contant = {
                                'grip_file':str(grip_file),
                                'script_file':str(script_file),
                                'pipe_name':str(pipeline_name),
                                'team_number':int(team_number),
                                'width':int(width),
                                'height':int(height),
                                'fps':int(fps)
                        }
                        json_file = json.dumps(contant)
                        ssh_client.exec_command("echo '" + json_file + "' > ~/.hawk/config.json")
                        get_label('label_settings_logger').setText("done!")
                except Exception as e:
                        connection_lost('label_settings_logger')
                        print(e)

        def entry_camera_reset_changed(arg):
                digits_only('entry_reset_camera')

        def button_reset_camera_clicked(arg):
                delete_file('cameras/' + get_entry('entry_reset_camera').text() + '.json')
                update_file_manager()

        def button_script_push_clicked(arg):
                local_path =  QFileDialog.getOpenFileName(layout, 'Choose script file')[0]
                file_name = local_path.split('/')[len(local_path.split('/'))-1]
                send_file(local_path, '~/.hawk/scripts/' + file_name)
                update_file_manager()

        def button_script_delete_clicked(arg):
                delete_file('scripts/' + get_combobox('combobox_fm_scripts').currentText())
                update_file_manager()

        def button_grip_push_clicked(arg):
                local_path =  QFileDialog.getOpenFileName(layout, 'Choose grip file')[0]
                file_name = local_path.split('/')[len(local_path.split('/'))-1]
                send_file(local_path, '~/.hawk/grips/' + file_name)
                update_file_manager()

        def button_grip_delete_clicked(arg):
                delete_file('grips/' + get_combobox('combobox_fm_grips').currentText())
                update_file_manager()

        def button_update_software_clicked(arg):
                try:
                        ssh_client.exec_command('cd hawk-vision/;  git fetch --all; git reset --hard origin/master; cd ~')
                        get_label('label_control_logger').setText("pulled software")
                except Exception as e:
                        connection_lost('label_control_logger')
                        print(e)

        def button_change_dns_clicked(arg):
                try:
                        name = get_entry('entry_change_dns').text()
                        ssh_client.exec_command('hostnamectl set-hostname ' + name)
                        get_label('label_control_logger').setText('DNS changed please reboot to commit')	
                except Exception as e:
                        connection_lost('label_control_logger')
                        print(e)

        def button_set_ip_clicked(arg):
                try:
                        address = get_entry('entry_set_ip').text() 
                        ssh_client.exec_command('~/hawk-vision/scripts/set_static_ip.sh ' + address)
                        get_label('label_control_logger').setText('changed address please reboot and log with ip address')
                except Exception as e:
                        connection_lost('label_control_logger')
                        print(e)

        def button_set_dhcp_clicked(arg):
                try:
                        ssh_client.exec_command('~/hawk-vision/scripts/remove_static_ip.sh')
                        get_label('label_control_logger').setText('changed to dhcp please reboot')	
                except Exception as e:
                        connection_lost('label_control_logger')
                        print(e)

        def start_config_clicked(arg):
                import Config_controller
                if get_prev_value() or get_next_value() or get_set_conf_value() or get_add_pt_value() or get_done_value():
                 changed_values(ssh_client)

                

        layout.button_connect.clicked.connect(button_connect_clicked)
        layout.button_set_ip.clicked.connect(button_set_ip_clicked)
        layout.button_set_dhcp.clicked.connect(button_set_dhcp_clicked)
        layout.change_password.clicked.connect(button_change_password_clicked)
        layout.entry_camera_number.textChanged.connect(entry_camera_number_changed)
        layout.button_calibrate_camera.clicked.connect(button_calibrate_camera_clicked)
        layout.button_reboot.clicked.connect(button_reboot_clicked)
        layout.entry_team_number.textChanged.connect(entry_team_number_changed)
        layout.entry_width.textChanged.connect(entry_width_changed)
        layout.entry_height.textChanged.connect(entry_height_changed)
        layout.entry_fps.textChanged.connect(entry_fps_changed)
        layout.button_save.clicked.connect(button_save_clicked)
        layout.entry_reset_camera.textChanged.connect(entry_camera_reset_changed)
        layout.button_reset_camera.clicked.connect(button_reset_camera_clicked)
        layout.button_push_script.clicked.connect(button_script_push_clicked)
        layout.button_delete_script.clicked.connect(button_script_delete_clicked)
        layout.button_push_grip.clicked.connect(button_grip_push_clicked)
        layout.button_delete_grip.clicked.connect(button_grip_delete_clicked)
        layout.button_update_software.clicked.connect(button_update_software_clicked)
        layout.button_change_dns.clicked.connect(button_change_dns_clicked)
        layout.button_refresh_browser.clicked.connect(button_refresh_camera_clicked)
        layout.start_config.clicked.connect(start_config_clicked)

        layout.Logo.setPixmap(QPixmap(path + '/ui/images/HawkEye.png'))
        layout.show()
        sys.exit(hawk_controller.exec())
