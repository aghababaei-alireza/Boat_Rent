from Boat import Boat

class MotorBoat(Boat):
    RENT_PRICE = 200000
    LAKE_PRICE = 100000

    def __init__(self, boat_id, 
                 color, 
                 owner_id, 
                 passenger_count, 
                 body_status,
                 full_fuel):
        self.boat_id = boat_id
        self.color = color
        self.owner_id = owner_id
        self.passenger_count = passenger_count
        self.body_status = body_status
        self.full_fuel = full_fuel

    def calculate_rent_price(self, time, is_rent):
        pass