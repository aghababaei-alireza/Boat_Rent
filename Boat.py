from abc import ABC, abstractmethod

class Boat(ABC):
    RENT_PRICE = 0
    LAKE_PRICE = 0
    
    def __init__(self, boat_id, 
                 color, 
                 owner_id, 
                 passenger_count, 
                 body_status):
        self.boat_id = boat_id
        self.color = color
        self.owner_id = owner_id
        self.passenger_count = passenger_count
        self.body_status = body_status

    @abstractmethod
    def calculate_rent_price(self, time, is_rent):
        pass