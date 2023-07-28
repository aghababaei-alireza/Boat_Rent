class Tourist:
    def __init__(self, tourist_id: int = 0,
                 name: str = "",
                 family: str = "",
                 mobile: str = "",
                 boat_id_list: list = []):
        self.tourist_id = tourist_id
        self.name = name
        self.family = family
        self.mobile = mobile
        self.boat_id_list = boat_id_list