from UI.Ui_MainWindow import Ui_MainWindow
from UI.Ui_TouristDialog import Ui_TouristDialog
from UI.Ui_BoatDialog import Ui_BoatDialog
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QPushButton
from Boat import Boat
from MotorBoat import MotorBoat
from PedalBoat import PedalBoat
from RowBoat import RowBoat
from Rent import Rent
from Tourist import Tourist

class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setupUi(self)
        
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
            
            self.tbl_available_boats.setItem(i, 0, QTableWidgetItem()) # Function

    def create_rent_button(self, boat: Boat):
        btn = QPushButton("اجاره")

    def btn_rent_clicked(self, boat: Boat):
        if len(self.tbl_tourists.selectedItems()) == 0:
            return # TODO Show Error to select tourist
        selected_row = self.tbl_tourists.selectedItems()[0].row()
        tourist_id = int(self.tbl_tourists.item(selected_row, 0))
        rent = Rent(boat=boat, tourist=Tourist(tourist_id), rent_time=None)