from abc import ABC, abstractmethod
from DatabaseManager import DatabaseManager

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
    def get_boat_by_id(cls, boat_id):
        cursor = DatabaseManager.get_cursor()
        cursor.execute("""SELECT b.BoatId, bt.BoatTypeName, b.Color, b.OwnerId, b.PassengerCount, b.BodyStatus, b.FullFuel, b.PaddleCount, b.PedalStatus 
                       FROM Boat AS b
                       INNER JOIN BoatType AS bt ON b.BoatTypeId = bt
                       .BoatTypeId WHERE BoatId = ?""", boat_id)
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
                from MotorBoat import MotorBoat
                return MotorBoat(boat_id, color, owner_id, passenger_count, body_status, full_fuel)
            case "پدالی":
                from PedalBoat import PedalBoat
                return PedalBoat(boat_id, color, owner_id, passenger_count, body_status, pedal_status)
            case "پارویی":
                from RowBoat import RowBoat
                return RowBoat(boat_id, color, owner_id, passenger_count, body_status, paddle_count)
            
    