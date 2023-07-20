from Boat import Boat


class RowBoat(Boat):
    RENT_PRICE = 140000
    LAKE_PRICE = 70000

    def __init__(self, boat_id, 
                 color, 
                 owner_id, 
                 passenger_count, 
                 body_status,
                 paddle_count):
        self.boat_id = boat_id
        self.color = color
        self.owner_id = owner_id
        self.passenger_count = passenger_count
        self.body_status = body_status
        self.paddle_count = paddle_count

    def calculate_rent_price(self, time, is_rent):
        pass