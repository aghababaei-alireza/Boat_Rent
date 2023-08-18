from UI.Ui_MainWindow import Ui_MainWindow
from UI.DateTimeDialog import DateTimeDialog
from UI.MessageDialog import MessageDialog
from UI.TouristDialog import TouristDialog
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QPushButton
from Boat import Boat
from MotorBoat import MotorBoat
from PedalBoat import PedalBoat
from RowBoat import RowBoat
from Rent import Rent
from Tourist import Tourist
from UI.BoatDialog import BoatDialog
from UI.StatDialog import StatDialog

class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setupUi(self)
        self.update()
        self.btn_add_tourist.clicked.connect(self.btn_add_tourist_clicked)
        self.btn_edit_tourist.clicked.connect(self.btn_edit_tourist_clicked)
        self.btn_delete_tourist.clicked.connect(self.btn_delete_tourist_clicked)
        self.btn_add_boat.clicked.connect(self.btn_add_boat_clicked)
        self.btn_edit_boat.clicked.connect(self.btn_edit_boat_clicked)
        self.btn_delete_boat.clicked.connect(self.btn_delete_boat_clicked)
        self.btn_calculate.clicked.connect(self.btn_calculate_clicked)
        
    def update_available_boats(self):
        self.available_boats = Boat.get_available_boats()
        self.lbl_available_boats_count.setText(str(len(self.available_boats)))

        # Clear the table
        self.tbl_available_boats.setRowCount(0)

        # Fill the table
        for i in range(len(self.available_boats)):
            boat = self.available_boats[i]
            self.tbl_available_boats.insertRow(i)

            self.tbl_available_boats.setItem(i, 1, QTableWidgetItem(str(boat.boat_id))) # Boat Id
            if isinstance(boat, MotorBoat):
                self.tbl_available_boats.setItem(i, 2, QTableWidgetItem('موتوری')) # Boat Type
                self.tbl_available_boats.setItem(i, 7, QTableWidgetItem(f"وضعیت بنزین: {'پر' if boat.full_fuel else 'خالی'}")) # Specific Field
            elif isinstance(boat, PedalBoat):
                self.tbl_available_boats.setItem(i, 2, QTableWidgetItem('پدالی')) # Boat Type
                self.tbl_available_boats.setItem(i, 7, QTableWidgetItem(f"وضعیت پدال: {'سالم' if boat.pedal_status else 'آسیب‌دیده'}")) # Specific Field
            elif isinstance(boat, RowBoat):
                self.tbl_available_boats.setItem(i, 2, QTableWidgetItem('پارویی')) # Boat Type
                self.tbl_available_boats.setItem(i, 7, QTableWidgetItem(f"تعداد پارو: {boat.paddle_count}")) # Specific Field
            self.tbl_available_boats.setItem(i, 3, QTableWidgetItem(boat.color)) # Boat Color
            self.tbl_available_boats.setItem(i, 4, QTableWidgetItem(str(boat.owner_id))) # Owner ID
            self.tbl_available_boats.setItem(i, 5, QTableWidgetItem(str(boat.passenger_count))) # Passenger Count
            self.tbl_available_boats.setItem(i, 6, QTableWidgetItem('سالم' if boat.body_status else 'آسیب‌دیده')) # Body Status
            
            self.tbl_available_boats.setCellWidget(i, 0, self.create_rent_button(boat)) # Function

    def create_rent_button(self, boat: Boat):
        btn = QPushButton("اجاره")
        btn.clicked.connect(lambda: self.btn_rent_clicked(boat))
        return btn

    def btn_rent_clicked(self, boat: Boat):
        if len(self.tbl_tourists.selectedItems()) == 0:
            MessageDialog(self, "ابتدا گردشگر اجاره‌کننده را از جدول گردشگران انتخاب کنید.").exec()
            return
        selected_row = self.tbl_tourists.selectedItems()[0].row()
        tourist_id = int(self.tbl_tourists.item(selected_row, 0).text())

        dlg_datetime = DateTimeDialog(self)
        (res, dt) = dlg_datetime.exec()
        if res == dlg_datetime.Rejected:
            return
        rent = Rent(boat=boat, tourist=Tourist(tourist_id))
        if rent.start_rent(dt):
            MessageDialog(self, f"قایق با کد {rent.boat.boat_id} توسط گردشگر با کد {rent.tourist.tourist_id} اجاره شد.").exec()
            self.update()
        else:
            MessageDialog(self, "در حال حاضر ظرفیت دریاچه تکمیل است.").exec()

    def update_rented_boats(self):
        self.rent_items = Rent.get_rented_boats()
        self.lbl_rented_boats_count.setText(str(len(self.rent_items)))

        # Clear the table
        self.tbl_rented_boats.setRowCount(0)

        # Fill the table
        for i in range(len(self.rent_items)):
            rent = self.rent_items[i]
            self.tbl_rented_boats.insertRow(i)

            self.tbl_rented_boats.setItem(i, 1, QTableWidgetItem(str(rent.rent_id))) # rent Id
            self.tbl_rented_boats.setItem(i, 2, QTableWidgetItem(str(rent.boat.boat_id))) # Boat Id

            if isinstance(rent.boat, MotorBoat):
                self.tbl_rented_boats.setItem(i, 3, QTableWidgetItem('موتوری')) # Boat Type
            elif isinstance(rent.boat, PedalBoat):
                self.tbl_rented_boats.setItem(i, 3, QTableWidgetItem('پدالی')) # Boat Type
            elif isinstance(rent.boat, RowBoat):
                self.tbl_rented_boats.setItem(i, 3, QTableWidgetItem('پارویی')) # Boat Type

            self.tbl_rented_boats.setItem(i, 4, QTableWidgetItem(rent.boat.color)) # Boat Color
            self.tbl_rented_boats.setItem(i, 5, QTableWidgetItem(str(rent.boat.owner_id))) # Owner Id
            self.tbl_rented_boats.setItem(i, 6, QTableWidgetItem(str(rent.tourist.tourist_id))) # Tourist Id
            self.tbl_rented_boats.setItem(i, 7, QTableWidgetItem(rent.rent_time.strftime("%Y/%m/%d - %H:%M"))) # Rent Time
            
            self.tbl_rented_boats.setCellWidget(i, 0, self.create_return_button(rent)) # Function

    def create_return_button(self, rent: Rent):
        btn = QPushButton("بازگرداندن")
        btn.clicked.connect(lambda: self.btn_return_boat_clicked(rent))
        return btn
    
    def btn_return_boat_clicked(self, rent: Rent):
        dlg_datetime = DateTimeDialog(self)
        (res, dt) = dlg_datetime.exec()
        if res == dlg_datetime.Rejected:
            return
        rent.finish_rent(dt)
        MessageDialog(self, f"قایق با کد {rent.boat.boat_id} توسط گردشگر با کد {rent.tourist.tourist_id} بازگردانده شد.").exec()
        self.update()

    def update_tourists(self):
        self.tourists = Tourist.get_all_tourists()
        # Clear the table
        self.tbl_tourists.setRowCount(0)
        # Fill the table
        i = 0
        for tourist in self.tourists:
            self.tbl_tourists.insertRow(i)
            self.tbl_tourists.setItem(i, 0, QTableWidgetItem(str(tourist.tourist_id)))
            self.tbl_tourists.setItem(i, 1, QTableWidgetItem(tourist.name))
            self.tbl_tourists.setItem(i, 2, QTableWidgetItem(tourist.family))
            self.tbl_tourists.setItem(i, 3, QTableWidgetItem(tourist.mobile))
            i += 1
    
    def update(self):
        self.update_available_boats()
        self.update_rented_boats()
        self.update_tourists()

    def btn_add_tourist_clicked(self):
        TouristDialog(self).exec()
        self.update()

    def btn_edit_tourist_clicked(self):
        selected_rows = self.tbl_tourists.selectedItems()
        if selected_rows:
            id = int(self.tbl_tourists.item(selected_rows[0].row(), 0).text())
        else:
            id = None
        TouristDialog(self, True, id).exec()
        self.update()

    def btn_delete_tourist_clicked(self):
        selected_items = self.tbl_tourists.selectedItems()
        if not selected_items:
            MessageDialog(self, "ابتدا گردشگر مورد نظر را از جدول انتخاب نمایید.").exec()
            return
        if MessageDialog(self, "آیا از حذف این گردشگر و تمام قایق‌های او اطمینان دارید؟", True).exec() == MessageDialog.Rejected:
            return
        tourist_id = int(self.tbl_tourists.item(selected_items[0].row(), 0).text())
        Tourist.delete_tourist(tourist_id)
        MessageDialog(self, "اطلاعات گردشگر به همراه تمام قایق‌های او با موفقیت حذف شد.").exec()
        self.update()


    def btn_add_boat_clicked(self):
        BoatDialog(self, 'create').exec()
        self.update()

    def btn_edit_boat_clicked(self):
        BoatDialog(self, 'edit').exec()
        self.update()

    def btn_delete_boat_clicked(self):
        BoatDialog(self, 'delete').exec()
        self.update()

    def btn_calculate_clicked(self):
        selected_rows = self.tbl_tourists.selectedItems()
        if selected_rows:
            id = int(self.tbl_tourists.item(selected_rows[0].row(), 0).text())
        else:
            id = None
        StatDialog(self, id).exec()