from config_layout import Ui_MainWindow as conf_window
from layout import Ui_MainWindow

import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtGui import *
import PyQt5.QtGui
import sys
import os
class HawkEye_controller():

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ## PyQt defintions
        global ui
        app = QApplication(sys.argv)
        ui = Ui_MainWindow()
        MainWindow = QMainWindow()
        
        ui.setupUi(PyQt5.QtWidgets.QMainWindow())

        ## more defintions
        REFRESH_RATE = 500
        PORT_ZERO = 1181
        path = os.path.dirname(os.path.abspath(__file__))
        browser = QWebEngineView(QWidget())
        browser.show()
        ui.browser_area.setWidget(browser)
        connected = False
        address = ''
        ssh_client = None
        timer = QTimer()
        timer.timeout.connect(refresh)
        timer.setInterval(REFRESH_RATE)

        ui.button_connect.clicked.connect(button_connect_clicked)
        ui.button_set_ip.clicked.connect(button_set_ip_clicked)
        ui.button_set_dhcp.clicked.connect(button_set_dhcp_clicked)
        ui.change_password.clicked.connect(button_change_password_clicked)
        ui.entry_camera_number.textChanged.connect(entry_camera_number_changed)
        ui.button_calibrate_camera.clicked.connect(button_calibrate_camera_clicked)
        ui.button_reboot.clicked.connect(button_reboot_clicked)
        ui.entry_team_number.textChanged.connect(entry_team_number_changed)
        ui.entry_width.textChanged.connect(entry_width_changed)
        ui.entry_height.textChanged.connect(entry_height_changed)
        ui.entry_fps.textChanged.connect(entry_fps_changed)
        ui.button_save.clicked.connect(button_save_clicked)
        ui.entry_reset_camera.textChanged.connect(entry_camera_reset_changed)
        ui.button_reset_camera.clicked.connect(button_reset_camera_clicked)
        ui.button_push_script.clicked.connect(button_script_push_clicked)
        ui.button_delete_script.clicked.connect(button_script_delete_clicked)
        ui.button_push_grip.clicked.connect(button_grip_push_clicked)
        ui.button_delete_grip.clicked.connect(button_grip_delete_clicked)
        ui.button_update_software.clicked.connect(button_update_software_clicked)
        ui.button_change_dns.clicked.connect(button_change_dns_clicked)
        ui.button_refresh_browser.clicked.connect(button_refresh_camera_clicked)
        ui.start_config.clicked.connect(start_config_clicked)
        ui.Logo.setPixmap(QPixmap(path + '/ui/images/HawkEye.png'))

    ##Start of hawkEye controller methods
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
        configWindow = conf_window()
        configWindow.setupUi(self)
        configWindow.exec_()
        print("shut up")
    ## END of hawk controller

    ## START of config controller
    global address
    prev_value,next_value,set_conf_value,add_pt_value,done_value = False,False,False,False,False
    url = 'http://' + address + ":1191/stream.mjpg"
    browser.load(QUrl(url))
    print(url)
    c_ui = conf_window()
    c_ui.setupUi(conf_window)
    #get values for main use
    def get_prev_value():
        if prev_value:
            prev_value = False
            return True
        return False
    def get_next_value():
        if next_value:
            next_value = False
            return True
        return False
    def get_set_conf_value():
        if set_conf_value:
            set_conf_value = False
            return True
        return False
    def get_add_pt_value():
        if add_pt_value:
            add_pt_value = False
            return True
        return False
    def get_done_value():
        if done_value:
            done_value = False
            return True
        return False
    def prev_click(arg):
        prev_value = True
    def next_click(arg):
        next_value = True
    def setConf_click(arg):
        set_conf_value = True
    def addPt_click(arg):
        add_pt_value = True
    def button_done_clicked(arg):
        done_value = True
        os.system('python3 hawk_controller.py')
        time.sleep(2)
        exit(0)
    
    def changed_values(ssh_client):
     ssh_client.exec_command("python3 -c'import main;main.changed_vals(" +get_prev_value()+','+get_next_value()+','+get_set_conf_value()+','+get_add_pt_value()+','+ get_done_value()+')')
     input("what?")

    def ischanged():
        return get_prev_value() or get_next_value() or get_set_conf_value() or get_add_pt_value() or get_done_value()
    c_ui.button_done.clicked.connect(button_done_clicked)
    c_ui.button_next.clicked.connect(next_click)
    c_ui.button_Previous.clicked.connect(prev_click)
    c_ui.button_setConfig.clicked.connect(setConf_click)
    c_ui.button_addPoint.clicked.connect(addPt_click)
    hawkEye_config_controller.aboutToQuit.connect(button_done_clicked)
    ## END of config controller

        #This part is for Config controller ONLY
    MainWindow.show()
    sys.exit(app.exec_())