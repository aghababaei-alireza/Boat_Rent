from UI.MainWindow import MainWindow
from PyQt5.QtWidgets import QApplication
import sys
from DatabaseManager import DatabaseManager
from UI.MessageDialog import MessageDialog

app = QApplication(sys.argv)
try:
    if not DatabaseManager.check_database_exists():
        DatabaseManager.create_database()
        MessageDialog(None, "پایگاه داده ایجاد شد.").exec()
except:
    MessageDialog(None, "ارتباط با پایگاه داده برقرار نشد.").exec()
w = MainWindow()
w.showMaximized()
app.exec()