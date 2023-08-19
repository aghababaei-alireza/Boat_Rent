from UI.MainWindow import MainWindow
from PyQt5.QtWidgets import QApplication
import sys
from DatabaseManager import DatabaseManager
from UI.MessageDialog import MessageDialog

app = QApplication(sys.argv)
if not DatabaseManager.check_database_exists():
    DatabaseManager.create_database()
    MessageDialog(None, "پایگاه داده ایجاد شد.").exec()
w = MainWindow()
w.showMaximized()
app.exec()