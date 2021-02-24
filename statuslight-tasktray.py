import os
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction

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
menulist_tray.addAction(action_Red)
#Yellow Button
action_Yellow = QAction(QIcon(os.path.join(icon_path, "Yellow.png")), "Yellow")
menulist_tray.addAction(action_Yellow)
#Green Button
action_Green = QAction(QIcon(os.path.join(icon_path, "Green.png")), "Green")
menulist_tray.addAction(action_Green)
#Off Button
#Green Button
action_Off = QAction( "Off")
menulist_tray.addAction(action_Off)

#add a separtor
menulist_tray.addSeparator()

#Refresh
actionHelp = QAction("Refresh")
menulist_tray.addAction(actionHelp)

#Quit the application
actionQuit = QAction("Quit")
menulist_tray.addAction(actionQuit)

#add a separator
menulist_tray.addSeparator()

tray_menu.setContextMenu(menulist_tray)

tray_app.exec_()