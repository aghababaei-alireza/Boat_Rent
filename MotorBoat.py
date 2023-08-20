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