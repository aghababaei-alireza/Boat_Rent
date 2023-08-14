from Boat import Boat
from DatabaseManager import DatabaseManager

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
        cursor.execute("""INSERT INTO Boat (BoatTypeId, Color, OwnerId, PassengerCount, BodyStatus, FullFuel, PaddleCount, PedalStatus)
                       OUTPUT INSERTED.BoatId
                       VALUES (?,?,?,?,?,1,?,1)""", 3, color, owner_id, passenger_count, body_status, paddle_count)
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