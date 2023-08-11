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

        if Rent.get_rented_boat_count() >= 20:
            return

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

        is_rent = not self.boat.owner_id == self.tourist.tourist_id 

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

    @classmethod
    def get_rented_boat_count(cls):
        cursor = DatabaseManager.get_cursor()
        cursor.execute("""SELECT COUNT(*) FROM Rent WHERE ReturnTime IS NULL""")
        return int(cursor.fetchval())
    
    @classmethod
    def get_rented_boats(cls):
        cursor = DatabaseManager.get_cursor()
        cursor.execute("""SELECT R.RentId, B.BoatId, BT.BoatTypeName, B.Color, B.OwnerId, B.PassengerCount, B.BodyStatus, B.FullFuel, B.PedalStatus, B.PaddleCount, T.TouristId, T.Name, T.Family, T.Mobile, R.RentTime
                        FROM Rent AS R
                        INNER JOIN Boat AS B ON R.BoatId = B.BoatId
                        INNER JOIN Tourist AS T ON R.TouristId = T.TouristId
                        WHERE ReturnTime IS NULL""")

        rent_items = []
        for item in cursor:
            rent_id = int(item[0])
            boat_id = int(item[1])
            boat_type_name = item[2]
            color = item[3]
            owner_id = int(item[4])
            passenger_count = int(item[5])
            body_status = bool(item[6])
            full_fuel = bool(item[7])
            pedal_status = bool(item[8])
            paddle_count = int(item[9])
            tourist_id = int(item[10])
            name = item[11]
            family = item[12]
            mobile = item[13]
            rent_time = datetime.fromisoformat(item[14])

            match boat_type_name:
                case "موتوری":
                    from MotorBoat import MotorBoat
                    boat = MotorBoat(boat_id, color, owner_id, passenger_count, body_status, full_fuel)
                case "پدالی":
                    from PedalBoat import PedalBoat
                    boat = PedalBoat(boat_id, color, owner_id, passenger_count, body_status, pedal_status)
                case "پارویی":
                    from RowBoat import RowBoat
                    boat = RowBoat(boat_id, color, owner_id, passenger_count, body_status, paddle_count)

            tourist = Tourist(tourist_id, name, family, mobile)
            rent_items.append(Rent(rent_id, boat, tourist, rent_time))

        return rent_items
    
