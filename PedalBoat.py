from Boat import Boat
from DatabaseManager import DatabaseManager

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