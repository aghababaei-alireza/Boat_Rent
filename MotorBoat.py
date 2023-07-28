from Boat import Boat
from DatabaseManager import DatabaseManager

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
    def create_new_motor_boat(cls, color, owner_id, passenger_count, body_status, full_fuel):
        cursor = DatabaseManager.get_cursor()
        cursor.execute("""INSERT INTO Boat (BoatTypeId, Color, OwnerId, PassengerCount, BodyStatus, FullFuel, PaddleCount, PedalStatus)
                       VALUES (?,?,?,?,?,?,0,1)""")
        cursor.commit()