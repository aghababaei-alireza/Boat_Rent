from Boat import Boat

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

    