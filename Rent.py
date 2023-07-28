from Boat import Boat
from Tourist import Tourist
from datetime import datetime
from DatabaseManager import DatabaseManager
from math import ceil

class Rent:
    OWNER_SHARE = 0.6
    LAKE_SHARE = 0.4

    def __init__(self,rent_id: int = 0,
                 boat: Boat = Boat(),
                 tourist: Tourist = Tourist(),
                 rent_time: datetime = None,
                 return_time: datetime = None,
                 owner_income: int = None,
                 lake_income: int = None):
        self.rent_id = rent_id
        self.boat = boat
        self.tourist = tourist
        self.rent_time = rent_time
        self.return_time = return_time
        self.owner_income = owner_income
        self.lake_income = lake_income

    def set_owner_share_income(self, price, is_rent):
        self.owner_income = (price * self.OWNER_SHARE) if is_rent else 0

    def set_lake_share_income(self, price, is_rent):
        self.lake_income = (price * self.LAKE_SHARE) if is_rent else price

    def start_rent(self, rent_time):
        if not self.rent_time:
            self.rent_time = rent_time
        cursor = DatabaseManager.get_cursor()
        cursor.execute("INSERT INTO Rent (BoatId, TouristId, RentTime) OUTPUT INSERTED.RentId VALUES (?, ?, ?)",
                       self.boat.id,
                       self.tourist.id,
                       self.rent_time.isoformat())
        self.rent_id = int(cursor.fetchval())
        cursor.commit()


    def finish_rent(self, return_time):
        if not self.return_time:
            self.return_time = return_time

        duration = (self.return_time - self.rent_time).total_seconds() / 3600
        hours = ceil(duration)

        is_rent = not self.boat.owner_id == self.tourist.id
        total_price = self.boat.calculate_rent_price(hours, is_rent)
        self.set_owner_share_income(total_price, is_rent)
        self.set_lake_share_income(total_price, is_rent)
        
        cursor = DatabaseManager.get_cursor()
        cursor.execute("UPDATE Rent SET ReturnTime = ?, OwnerIncome = ?, LakeIncome = ? WHERE RentId = ?",
                       self.return_time.isoformat(),
                       self.owner_income,
                       self.lake_income,
                       self.rent_id)
        cursor.commit()