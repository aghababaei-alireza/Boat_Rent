from Core import *

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

    def start_rent(self, rent_time) -> bool:
        if not self.rent_time:
            self.rent_time = rent_time
        
        if Rent.get_rented_boat_count() >= 20:
            return -1
        
        if not Tourist.is_tourist_available(self.tourist.tourist_id):
            return -2

        cursor = DatabaseManager.get_cursor()
        cursor.execute("INSERT INTO Rent (BoatId, TouristId, RentTime) OUTPUT INSERTED.RentId VALUES (?, ?, ?)",
                       self.boat.boat_id,
                       self.tourist.tourist_id,
                       self.rent_time.isoformat())
        self.rent_id = int(cursor.fetchval())
        cursor.commit()
        return self.rent_id

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
    def get_rented_boat_count(cls) -> int:
        cursor = DatabaseManager.get_cursor()
        cursor.execute("""SELECT COUNT(*) FROM Rent WHERE ReturnTime IS NULL""")
        return int(cursor.fetchval())
    
    @classmethod
    def get_rented_boats(cls) -> list['Rent']:
        cursor = DatabaseManager.get_cursor()
        cursor.execute("""SELECT R.RentId, B.BoatId, BT.BoatTypeName, B.Color, B.OwnerId, B.PassengerCount, B.BodyStatus, B.FullFuel, B.PedalStatus, B.PaddleCount, T.TouristId, T.Name, T.Family, T.Mobile, R.RentTime
                        FROM Rent AS R
                        INNER JOIN Boat AS B ON R.BoatId = B.BoatId
                        INNER JOIN BoatType AS BT ON B.BoatTypeId = BT.BoatTypeId
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
            rent_time = item[14]

            match boat_type_name:
                case "موتوری":
                    boat = MotorBoat(boat_id, color, owner_id, passenger_count, body_status, full_fuel)
                case "پدالی":
                    boat = PedalBoat(boat_id, color, owner_id, passenger_count, body_status, pedal_status)
                case "پارویی":
                    boat = RowBoat(boat_id, color, owner_id, passenger_count, body_status, paddle_count)

            tourist = Tourist(tourist_id, name, family, mobile)
            rent_items.append(Rent(rent_id, boat, tourist, rent_time))

        return rent_items
    
    @classmethod
    def calculate_owner_income(cls, owner_id: int, datetime_from: datetime, datetime_to: datetime) -> list['Rent']:
        cursor = DatabaseManager.get_cursor()
        cursor.execute("""SELECT R.RentId, B.BoatId, B.OwnerId, R.TouristId, R.RentTime, R.ReturnTime, R.OwnerIncome, R.LakeIncome 
                       FROM Rent AS R
                       INNER JOIN Boat AS B ON R.BoatId = B.BoatId
                       WHERE R.ReturnTime IS NOT NULL AND B.OwnerId = ? AND 
                       (R.RentTime BETWEEN ? AND ?) AND (R.ReturnTime BETWEEN ? AND ?)""",
                       owner_id, datetime_from, datetime_to, datetime_from, datetime_to)
        rent_items = []
        for row in cursor:
            rent_id = int(row[0])
            boat = Boat(boat_id=int(row[1]), owner_id=int(row[2]))
            tourist = Tourist(tourist_id=int(row[3]))
            rent_time = row[4]
            return_time = row[5]
            owner_income = int(row[6])
            lake_income = int(row[7])
            rent_items.append(Rent(rent_id, boat, tourist, rent_time, return_time, owner_income, lake_income))
        return rent_items

    @classmethod
    def calculate_lake_income(cls, datetime_from: datetime, datetime_to: datetime) -> list['Rent']:
        cursor = DatabaseManager.get_cursor()
        cursor.execute("""SELECT R.RentId, B.BoatId, B.OwnerId, R.TouristId, R.RentTime, R.ReturnTime, R.OwnerIncome, R.LakeIncome 
                       FROM Rent AS R
                       INNER JOIN Boat AS B ON R.BoatId = B.BoatId
                       WHERE R.ReturnTime IS NOT NULL AND 
                       (R.RentTime BETWEEN ? AND ?) AND (R.ReturnTime BETWEEN ? AND ?)""",
                       datetime_from, datetime_to, datetime_from, datetime_to)
        rent_items = []
        for row in cursor:
            rent_id = int(row[0])
            boat = Boat(boat_id=int(row[1]), owner_id=int(row[2]))
            tourist = Tourist(tourist_id=int(row[3]))
            rent_time = row[4]
            return_time = row[5]
            owner_income = int(row[6])
            lake_income = int(row[7])
            rent_items.append(Rent(rent_id, boat, tourist, rent_time, return_time, owner_income, lake_income))
        return rent_items

    @classmethod
    def calculate_owner_daily_income(cls, owner_id: int, datetime_from: datetime, datetime_to: datetime) -> dict:
        cursor = DatabaseManager.get_cursor()
        cursor.execute("""SELECT CAST(R.ReturnTime AS DATE) AS RentDate, SUM(R.OwnerIncome)
                       FROM Rent AS R
                       INNER JOIN Boat AS B ON R.BoatId = B.BoatId
                       WHERE R.ReturnTime IS NOT NULL AND B.OwnerId = ? AND 
                       (R.RentTime BETWEEN ? AND ?) AND (R.ReturnTime BETWEEN ? AND ?)
                       GROUP BY CAST(R.ReturnTime AS DATE)
                       ORDER BY RentDate""",
                       owner_id, datetime_from, datetime_to, datetime_from, datetime_to)
        daily_incomes = {}
        for row in cursor:
            date = datetime.fromisoformat(row[0])
            income = int(row[1])
            daily_incomes[date] = income
        return daily_incomes

    @classmethod
    def calculate_lake_daily_income(cls, datetime_from: datetime, datetime_to: datetime) -> dict:
        cursor = DatabaseManager.get_cursor()
        cursor.execute("""SELECT CAST(R.ReturnTime AS DATE) AS RentDate, SUM(R.LakeIncome)
                       FROM Rent AS R
                       INNER JOIN Boat AS B ON R.BoatId = B.BoatId
                       WHERE R.ReturnTime IS NOT NULL AND
                       (R.RentTime BETWEEN ? AND ?) AND (R.ReturnTime BETWEEN ? AND ?)
                       GROUP BY CAST(R.ReturnTime AS DATE)
                       ORDER BY RentDate""",
                       datetime_from, datetime_to, datetime_from, datetime_to)
        daily_incomes = {}
        for row in cursor:
            date = datetime.fromisoformat(row[0])
            income = int(row[1])
            daily_incomes[date] = income
        return daily_incomes