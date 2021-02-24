import os
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction
import requests

def SendColorUpdate(color):
    
    url = "Enter your URL"
    querystring = {"Enter your URL parameters"}

    payload_tempalte = "{{\n\t\"color\": \"{}\"\n}}"
    payload = payload_tempalte.format(color)
    headers = {'content-type': 'application/json'}

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

    print(response.text)


#Initialize the application
tray_app = QApplication([])
tray_app.setQuitOnLastWindowClosed(False)

#Set the icon path
icon_path = os.path.join(os.path.dirname(__file__), "icons/")

#Set the application icon
tray_icon = QIcon(os.path.join(icon_path, "statuslight.png"))
tray_menu = QSystemTrayIcon()
tray_menu.setIcon(tray_icon)
tray_menu.setVisible(True)

#Initialize the menu 
menulist_tray = QMenu()
#Red Button
action_Red = QAction(QIcon(os.path.join(icon_path, "Red.png")), "Red")
action_Red.triggered.connect(lambda: SendColorUpdate("FF0000"))
menulist_tray.addAction(action_Red)
#Yellow Button
action_Yellow = QAction(QIcon(os.path.join(icon_path, "Yellow.png")), "Yellow")
action_Yellow.triggered.connect(lambda: SendColorUpdate("FFFF00"))
menulist_tray.addAction(action_Yellow)
#Green Button
action_Green = QAction(QIcon(os.path.join(icon_path, "Green.png")), "Green")
action_Green.triggered.connect(lambda: SendColorUpdate("00FF00"))
menulist_tray.addAction(action_Green)
#Off Button
#Green Button
action_Off = QAction( "Off")
action_Off.triggered.connect(lambda: SendColorUpdate("000000"))
menulist_tray.addAction(action_Off)

#add a separtor
menulist_tray.addSeparator()

#Refresh
action_Refresh = QAction("Refresh")
menulist_tray.addAction(action_Refresh)

#Quit the application
action_Quit = QAction("Quit")
action_Quit.triggered.connect(tray_app.quit)
menulist_tray.addAction(action_Quit)


#add a separator
menulist_tray.addSeparator()

tray_menu.setContextMenu(menulist_tray)

tray_app.exec_()