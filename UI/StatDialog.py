from UI.Ui_StatDialog import Ui_StatDialog
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QHeaderView
from datetime import datetime, timedelta
from Rent import Rent
from Tourist import Tourist
from UI.MessageDialog import MessageDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from typing import Literal

class StatDialog(Ui_StatDialog, QDialog):
    def __init__(self, parent = None, tourist_id: int = None):
        super(QDialog, self).__init__(parent)
        self.setupUi(self)
        self.lbl_error.setVisible(False)
        try:
            self.tourists_id = Tourist.get_all_tourists_id()
            self.cmb_tourist_id.clear()
            for id in self.tourists_id:
                self.cmb_tourist_id.addItem(str(id))
        except:
            MessageDialog(self, "ارتباط با پایگاه داده برقرار نشد.").exec()

        if tourist_id:
            self.rdb_tourist.setChecked(True)
            self.wgt_tourist_id.setVisible(True)
            self.cmb_tourist_id.setCurrentText(str(tourist_id))
        else:
            self.rdb_lake.setChecked(True)
            self.wgt_tourist_id.setVisible(False)

        self.rdb_tourist.toggled.connect(self.rdb_tourist_checked_changed)
        self.btn_calculate.clicked.connect(self.btn_calculate_clicked)

        self.spn_year_from.valueChanged.connect(lambda: self.lbl_error.setVisible(False))
        self.spn_month_from.valueChanged.connect(lambda: self.lbl_error.setVisible(False))
        self.spn_day_from.valueChanged.connect(lambda: self.lbl_error.setVisible(False))
        self.spn_year_to.valueChanged.connect(lambda: self.lbl_error.setVisible(False))
        self.spn_month_to.valueChanged.connect(lambda: self.lbl_error.setVisible(False))
        self.spn_day_to.valueChanged.connect(lambda: self.lbl_error.setVisible(False))

        self.tbl_income.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.vlay_plot.addWidget(self.canvas)
        self.rdb_line_plot.toggled.connect(lambda checked: self.plot_income(self.daily_incomes, 'line' if checked else 'bar'))

    def show_error(self, message: str):
        self.lbl_error.setText(message)
        self.lbl_error.setVisible(True)
    
    def rdb_tourist_checked_changed(self, checked):
        self.wgt_tourist_id.setVisible(checked)
        self.lbl_error.setVisible(False)

    def btn_calculate_clicked(self):
        year_from = self.spn_year_from.value()
        month_from = self.spn_month_from.value()
        day_from = self.spn_day_from.value()
        year_to = self.spn_year_to.value()
        month_to = self.spn_month_to.value()
        day_to = self.spn_day_to.value()
        try:
            datetime_from = datetime(year_from, month_from, day_from, 0,0,0)
            datetime_to = datetime(year_to, month_to, day_to, 23, 59, 59)
            if datetime_from > datetime_to:
                self.show_error("تاریخ دوم نمی‌تواند از تاریخ اول کوچکتر باشد")
                return
        except:
            self.show_error("تاریخ وارد شده نادرست است.")
            return
        
        try:
            if self.rdb_tourist.isChecked():
                if not self.cmb_tourist_id.currentText():
                    self.show_error("کد مالک نمی‌تواند خالی باشد")
                    return
                owner_id = int(self.cmb_tourist_id.currentText())
                self.rent_items = Rent.calculate_owner_income(owner_id, datetime_from, datetime_to)
            else:
                self.rent_items = Rent.calculate_lake_income(datetime_from, datetime_to)
            # Clear the table
            self.tbl_income.setRowCount(0)
            # Fill the table
            i = 0
            owner_income = 0
            lake_income = 0
            for rent in self.rent_items:
                self.tbl_income.insertRow(i)
                self.tbl_income.setItem(i, 0, QTableWidgetItem(str(rent.boat.boat_id))) # Boat Id
                self.tbl_income.setItem(i, 1, QTableWidgetItem(str(rent.boat.owner_id))) # Owner Id
                self.tbl_income.setItem(i, 2, QTableWidgetItem(str(rent.tourist.tourist_id))) # Tourist Id
                self.tbl_income.setItem(i, 3, QTableWidgetItem(rent.rent_time.strftime("%Y/%m/%d - %H:%M"))) # Rent Time
                self.tbl_income.setItem(i, 4, QTableWidgetItem(rent.return_time.strftime("%Y/%m/%d - %H:%M"))) # Return Time
                self.tbl_income.setItem(i, 5, QTableWidgetItem(f"{rent.owner_income:,}")) # Owner Income
                self.tbl_income.setItem(i, 6, QTableWidgetItem(f"{rent.lake_income:,}")) # Lake Income
                i += 1
                owner_income += rent.owner_income
                lake_income += rent.lake_income
            if self.rdb_tourist.isChecked():
                self.lbl_total_income.setText(f"{owner_income:,}")
                self.daily_incomes = Rent.calculate_owner_daily_income(owner_id, datetime_from, datetime_to)
            else:
                self.lbl_total_income.setText(f"{lake_income:,}")
                self.daily_incomes = Rent.calculate_lake_daily_income(datetime_from, datetime_to)
            d = datetime_from
            while d <= datetime_to:
                if d not in self.daily_incomes.keys():
                    self.daily_incomes[d] = 0
                d += timedelta(days=1)
            self.plot_income(self.daily_incomes, 'line' if self.rdb_line_plot.isChecked() else 'bar')
        except:
            MessageDialog(self, "ارتباط با پایگاه داده برقرار نشد.").exec()

    def plot_income(self, daily_income: dict, plot_type: Literal['line', 'bar']):
        if not daily_income:
            return
        x = sorted(daily_income.keys()).sort()
        y = [daily_income[k] for k in x]
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        match plot_type:
            case 'line':
                ax.plot(x, y)
            case 'bar':
                ax.bar(x, y)
        self.canvas.draw()