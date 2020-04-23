import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtGui import *
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))

address = "192.168.1.6:1181/stream.mjpg" #sys.argv[1]
path = os.path.dirname(os.path.abspath(__file__))
hawkEye_config_controller = QApplication([])
layout = uic.loadUi(path + "/ui/config_layout.ui")

browser = QWebEngineView()
layout.browser_area.setWidget(browser)

prev_value,next_value,set_conf_value,add_pt_value,done_value = False,False,False,False,False
url = 'http://' + address
browser.load(QUrl(url))
print(url)
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
    exit(0)
    
def changed_values(ssh_client):
 ssh_client.exec_command("python3 -c'import main;main.changed_vals(" +get_prev_value()+','+get_next_value()+','+get_set_conf_value()+','+get_add_pt_value()+','+ get_done_value()+')')
 input("what?")
layout.button_done.clicked.connect(button_done_clicked)
layout.button_next.clicked.connect(next_click)
layout.button_Previous.clicked.connect(prev_click)
layout.button_setConfig.clicked.connect(setConf_click)
layout.button_addPoint.clicked.connect(addPt_click)

layout.show()
#sys.exit(hawkEye_config_controller.exec())
