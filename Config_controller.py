import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtGui import *
import os
import sys

address = sys.argv[1]
path = os.path.dirname(os.path.abspath(__file__))
hawkEye_config_controller = QApplication([])
layout = uic.loadUi(path + "/ui/config_layout.ui")

browser = QWebEngineView()
layout.browser_area.setWidget(browser)

url = 'http://' + address
#browser.load(QUrl(url))
print(url)

def button_done_clicked(arg):
    exit(0)

layout.button_done.clicked.connect(button_done_clicked)

layout.show()
sys.exit(hawkEye_config_controller.exec())
