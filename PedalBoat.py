from Boat import Boat

class PedalBoat(Boat):
    RENT_PRICE = 100000
    LAKE_PRICE = 50000

    def __init__(self, boat_id, 
                 color, 
                 owner_id, 
                 passenger_count, 
                 body_status,
                 pedal_status):
        self.boat_id = boat_id
        self.color = color
        self.owner_id = owner_id
        self.passenger_count = passenger_count
        self.body_status = body_status
        self.pedal_status = pedal_status

    def calculate_rent_price(self, time, is_rent):
        pass