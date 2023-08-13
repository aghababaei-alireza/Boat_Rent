from UI.MainWindow import MainWindow
from UI.MessageDialog import MessageDialog
from UI.DateTimeDialog import DateTimeDialog
from PyQt5.QtWidgets import QApplication
import sys

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()