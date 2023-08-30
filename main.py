import sys
from Core import *
from UI import *

app = QApplication(sys.argv)
try:
    if not DatabaseManager.check_database_exists():
        DatabaseManager.create_database()
        MessageDialog(None, "پایگاه داده ایجاد شد.").exec()
except Exception as e:
    print(e)
    MessageDialog(None, "ارتباط با پایگاه داده برقرار نشد.").exec()
w = MainWindow()
w.showMaximized()
app.exec()