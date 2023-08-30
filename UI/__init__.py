# PyQt Imports
from PyQt5.QtWidgets import QDialog, QMainWindow, QTableWidgetItem, QPushButton, QHeaderView, QApplication

# Others
from typing import Literal
from datetime import datetime, timedelta
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import re

# Core Imports
from Core import *

# UI Imports
from UI.Ui_BoatDialog import Ui_BoatDialog
from UI.Ui_DateTimeDialog import Ui_DateTimeDialog
from UI.Ui_MainWindow import Ui_MainWindow
from UI.Ui_MessageDialog import Ui_MessageDialog
from UI.Ui_StatDialog import Ui_StatDialog
from UI.Ui_TouristDialog import Ui_TouristDialog

# Form Imports
from UI.MessageDialog import MessageDialog
from UI.DateTimeDialog import DateTimeDialog
from UI.TouristDialog import TouristDialog
from UI.BoatDialog import BoatDialog
from UI.StatDialog import StatDialog
from UI.MainWindow import MainWindow