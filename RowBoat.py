from Boat import Boat

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

