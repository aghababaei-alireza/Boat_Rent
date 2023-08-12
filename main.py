from UI.MainWindow import MainWindow
from PyQt5.QtWidgets import QApplication
import sys

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()