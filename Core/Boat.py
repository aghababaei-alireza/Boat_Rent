from Core import *

class Boat(ABC):
    RENT_PRICE = 0
    LAKE_PRICE = 0
    
    def __init__(self, boat_id: int = 0, 
                 color: str = "", 
                 owner_id: int = None, 
                 passenger_count: int = 4, 
                 body_status: bool = True):
        self.boat_id = boat_id
        self.color = color
        self.owner_id = owner_id
        self.passenger_count = passenger_count
        self.body_status = body_status

    def calculate_rent_price(self, time, is_rent):
        if is_rent:
            return time * self.RENT_PRICE
        return time * self.LAKE_PRICE
    
    @classmethod
    def get_boat_by_id(cls, boat_id) -> 'Boat':
        cursor = DatabaseManager.get_cursor()
        cursor.execute("""SELECT B.BoatId, BT.BoatTypeName, B.Color, B.OwnerId, B.PassengerCount, B.BodyStatus, B.FullFuel, B.PaddleCount, B.PedalStatus 
                       FROM Boat AS B
                       INNER JOIN BoatType AS BT ON B.BoatTypeId = BT.BoatTypeId 
                       WHERE B.BoatId = ? AND B.IsActive = 1""", boat_id)
        row = cursor.fetchone()
        if not row:
            return None
        boat_id = int(row[0])
        boat_type_name = row[1]
        color = row[2]
        owner_id = int(row[3])
        passenger_count = int(row[4])
        body_status = bool(row[5])
        full_fuel = bool(row[6])
        paddle_count = int(row[7])
        pedal_status = bool(row[8])

        match boat_type_name:
            case "موتوری":
                from Core import MotorBoat
                return MotorBoat(boat_id, color, owner_id, passenger_count, body_status, full_fuel)
            case "پدالی":
                from Core import PedalBoat
                return PedalBoat(boat_id, color, owner_id, passenger_count, body_status, pedal_status)
            case "پارویی":
                from Core import RowBoat
                return RowBoat(boat_id, color, owner_id, passenger_count, body_status, paddle_count)
            
    @classmethod
    def get_available_boats(cls) -> list['Boat']:
        cursor = DatabaseManager.get_cursor()
        cursor.execute("""
            SELECT B.BoatId, BT.BoatTypeName, B.Color, B.OwnerId, B.PassengerCount, B.BodyStatus, B.FullFuel, B.PaddleCount, B.PedalStatus
            FROM Boat AS B
            INNER JOIN BoatType AS BT ON B.BoatTypeId = BT.BoatTypeId
            LEFT JOIN Rent AS R ON R.BoatId = B.BoatId
            WHERE B.IsActive = 1 AND B.BoatId NOT IN (
                SELECT B.BoatId FROM Boat AS B 
                INNER JOIN Rent AS R ON B.BoatId = R.BoatId
                WHERE R.ReturnTime IS NULL
                GROUP BY B.BoatId
            ) 
            AND B.BodyStatus = 1 AND
            ((BT.BoatTypeName = N'موتوری' AND B.FullFuel = 1)
            OR (BT.BoatTypeName = N'پدالی' AND B.PedalStatus = 1)
            OR (BT.BoatTypeName = N'پارویی' AND B.PaddleCount >= 3))
            GROUP BY B.BoatId, BT.BoatTypeName, B.Color, B.OwnerId, B.PassengerCount, B.BodyStatus, B.FullFuel, B.PaddleCount, B.PedalStatus
        """)
        boats = []
        for row in cursor:
            boat_id = int(row[0])
            boat_type_name = row[1]
            color = row[2]
            owner_id = int(row[3])
            passenger_count = int(row[4])
            body_status = bool(row[5])
            full_fuel = bool(row[6])
            paddle_count = int(row[7])
            pedal_status = bool(row[8])

            match boat_type_name:
                case "موتوری":
                    from Core import MotorBoat
                    boats.append(MotorBoat(boat_id, color, owner_id, passenger_count, body_status, full_fuel))
                case "پدالی":
                    from Core import PedalBoat
                    boats.append(PedalBoat(boat_id, color, owner_id, passenger_count, body_status, pedal_status))
                case "پارویی":
                    from Core import RowBoat
                    boats.append(RowBoat(boat_id, color, owner_id, passenger_count, body_status, paddle_count))
        return boats

    @classmethod
    def get_all_boats(cls) -> list['Boat']:
        cursor = DatabaseManager.get_cursor()
        cursor.execute("""SELECT B.BoatId, BT.BoatTypeName, B.Color, B.OwnerId, B.PassengerCount, B.BodyStatus, B.FullFuel, B.PaddleCount, B.PedalStatus
                       FROM Boat AS B
                       INNER JOIN BoatType AS BT ON B.BoatTypeId = BT.BoatTypeId
                       WHERE B.IsActive = 1""")
        boats = []
        for row in cursor:
            boat_id = int(row[0])
            boat_type_name = row[1]
            color = row[2]
            owner_id = int(row[3])
            passenger_count = int(row[4])
            body_status = bool(row[5])
            full_fuel = bool(row[6])
            paddle_count = int(row[7])
            pedal_status = bool(row[8])

            match boat_type_name:
                case "موتوری":
                    from Core import MotorBoat
                    boats.append(MotorBoat(boat_id, color, owner_id, passenger_count, body_status, full_fuel))
                case "پدالی":
                    from Core import PedalBoat
                    boats.append(PedalBoat(boat_id, color, owner_id, passenger_count, body_status, pedal_status))
                case "پارویی":
                    from Core import RowBoat
                    boats.append(RowBoat(boat_id, color, owner_id, passenger_count, body_status, paddle_count))
        return boats
    
    @classmethod
    def delete_tourist_boats(cls, tourist_id):
        curosr = DatabaseManager.get_cursor()
        curosr.execute("""UPDATE Boat SET IsActive = 0 WHERE OwnerId = ?""", tourist_id)
        curosr.commit()

    @classmethod
    def delete_boat_by_id(cls, boat_id):
        curosr = DatabaseManager.get_cursor()
        curosr.execute("""UPDATE Boat SET IsActive = 0 WHERE BoatId = ?""", boat_id)
        curosr.commit()

class MotorBoat(Boat):
    RENT_PRICE = 200000
    LAKE_PRICE = 100000

    def __init__(self, boat_id: int = 0, 
                 color: str = "", 
                 owner_id: int = None, 
                 passenger_count: int = 4, 
                 body_status: bool = True,
                 full_fuel: bool = True):
        super().__init__(boat_id, color, owner_id, passenger_count, body_status)
        self.full_fuel = full_fuel

    @classmethod
    def create_new_motor_boat(cls, color, owner_id, passenger_count, body_status, full_fuel) -> int:
        cursor = DatabaseManager.get_cursor()
        cursor.execute("""INSERT INTO Boat (BoatTypeId, Color, OwnerId, PassengerCount, BodyStatus, FullFuel, PaddleCount, PedalStatus, IsActive)
                       OUTPUT INSERTED.BoatId
                       VALUES (1,?,?,?,?,?,0,1,1)""", color, owner_id, passenger_count, body_status, full_fuel)
        boat_id = int(cursor.fetchval())
        cursor.commit()
        return boat_id
    
    @classmethod
    def edit_motor_boat(cls, boat_id, color, owner_id, passenger_count, body_status, full_fuel):
        cursor = DatabaseManager.get_cursor()
        cursor.execute("""UPDATE Boat SET
                       BoatTypeId = 1, Color = ?, OwnerId = ?, PassengerCount = ?, BodyStatus = ?, FullFuel = ?, PaddleCount = 0, PedalStatus = 1
                       WHERE BoatId = ?""",
                       color, owner_id, passenger_count, body_status, full_fuel, boat_id)
        cursor.commit()

class PedalBoat(Boat):
    RENT_PRICE = 100000
    LAKE_PRICE = 50000

    def __init__(self, boat_id: int = 0, 
                 color: str = "", 
                 owner_id: int = None, 
                 passenger_count: int = 4, 
                 body_status: bool = True,
                 pedal_status: bool = True):
        super().__init__(boat_id, color, owner_id, passenger_count, body_status)
        self.pedal_status = pedal_status

    @classmethod
    def create_new_pedal_boat(cls, color, owner_id, passenger_count, body_status, pedal_status):
        cursor = DatabaseManager.get_cursor()
        cursor.execute("""INSERT INTO Boat (BoatTypeId, Color, OwnerId, PassengerCount, BodyStatus, FullFuel, PaddleCount, PedalStatus, IsActive)
                       OUTPUT INSERTED.BoatId
                       VALUES (?,?,?,?,?,1,0,?,1)""", 2, color, owner_id, passenger_count, body_status, pedal_status)
        boat_id = int(cursor.fetchval())
        cursor.commit()
        return boat_id
    
    @classmethod
    def edit_pedal_boat(cls, boat_id, color, owner_id, passenger_count, body_status, pedal_status):
        cursor = DatabaseManager.get_cursor()
        cursor.execute("""UPDATE Boat SET
                       BoatTypeId = 2, Color = ?, OwnerId = ?, PassengerCount = ?, BodyStatus = ?, FullFuel = 1, PaddleCount = 0, PedalStatus = ?
                       WHERE BoatId = ?""",
                       color, owner_id, passenger_count, body_status, pedal_status, boat_id)
        cursor.commit()

class RowBoat(Boat):
    RENT_PRICE = 140000
    LAKE_PRICE = 70000

    def __init__(self, boat_id: int = 0, 
                 color: str = "", 
                 owner_id: int = None, 
                 passenger_count: int = 4, 
                 body_status: bool = True,
                 paddle_count: int = 3):
        super().__init__(boat_id, color, owner_id, passenger_count, body_status)
        self.paddle_count = paddle_count

    @classmethod
    def create_new_row_boat(cls, color, owner_id, passenger_count, body_status, paddle_count):
        cursor = DatabaseManager.get_cursor()
        cursor.execute("""INSERT INTO Boat (BoatTypeId, Color, OwnerId, PassengerCount, BodyStatus, FullFuel, PaddleCount, PedalStatus, IsActive)
                       OUTPUT INSERTED.BoatId
                       VALUES (?,?,?,?,?,1,?,1,1)""", 3, color, owner_id, passenger_count, body_status, paddle_count)
        boat_id = int(cursor.fetchval())
        cursor.commit()
        return boat_id

    @classmethod
    def edit_row_boat(cls, boat_id, color, owner_id, passenger_count, body_status, paddle_count):
        cursor = DatabaseManager.get_cursor()
        cursor.execute("""UPDATE Boat SET
                       BoatTypeId = 3, Color = ?, OwnerId = ?, PassengerCount = ?, BodyStatus = ?, FullFuel = 1, PaddleCount = ?, PedalStatus = 1
                       WHERE BoatId = ?""",
                       color, owner_id, passenger_count, body_status, paddle_count, boat_id)
        cursor.commit()