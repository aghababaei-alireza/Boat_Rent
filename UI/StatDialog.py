from UI.Ui_StatDialog import Ui_StatDialog
from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from datetime import datetime
from Rent import Rent
from Tourist import Tourist
from UI.MessageDialog import MessageDialog

class StatDialog(Ui_StatDialog, QDialog):
    def __init__(self, parent = None, tourist_id: int = None):
        super(QDialog, self).__init__(parent)
        self.setupUi(self)

        # self.tourists_id = Tourist.get_all_tourists_id()
        # self.cmb_tourist_id.clear()
        # for id in self.tourists_id:
        #     self.cmb_tourist_id.addItem(str(id))

        if tourist_id:
            self.rdb_tourist.setChecked(True)
            self.wgt_tourist_id.setVisible(True)
        else:
            self.rdb_lake.setChecked(True)
            self.wgt_tourist_id.setVisible(False)

        self.rdb_tourist.toggled.connect(self.rdb_tourist_checked_changed)

    def rdb_tourist_checked_changed(self, checked):
        self.wgt_tourist_id.setVisible(checked)

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
        except:
            MessageDialog(self, "تاریخ وارد شده نادرست است.").exec()
            return
        if self.rdb_tourist.isChecked():
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
            self.tbl_income.setItem(i, 3, QTableWidgetItem(rent.rent_time.isoformat())) # Rent Time
            self.tbl_income.setItem(i, 4, QTableWidgetItem(rent.return_time.isoformat())) # Return Time
            self.tbl_income.setItem(i, 5, QTableWidgetItem(str(rent.owner_income))) # Owner Income
            self.tbl_income.setItem(i, 6, QTableWidgetItem(str(rent.lake_income))) # Lake Income
            i += 1
            owner_income += rent.owner_income
            lake_income += rent.lake_income
        if self.rdb_tourist.isChecked():
            self.lbl_total_income.setText(str(owner_income))
        else:
            self.lbl_total_income.setText(str(lake_income))
        
        # TODO Plot daily income