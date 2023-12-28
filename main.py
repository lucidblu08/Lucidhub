from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl
from PyQt6 import QtGui
import sys

app = QApplication(sys.argv)

autoUpdate = QWidget()
autoUpdate.setWindowTitle("Lucidhub - Updating")
autoUpdate.resize(600, 300)
layout = QVBoxLayout(autoUpdate)
autoUpdateLabel = QLabel("Updating please wait")
layout.addWidget(autoUpdateLabel)
autoUpdate.show()

view = QWebEngineView()
view.setWindowTitle("Lucidhub")
view.load(QUrl("http://lucidblu.000.pe/newindex"))
view.resize(1024, 750)
view.show()

app.setWindowIcon(QtGui.QIcon('connection.ico'))
view.setWindowIcon(QtGui.QIcon('connection.ico'))
app.exec()