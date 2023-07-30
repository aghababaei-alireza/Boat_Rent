from DatabaseManager import DatabaseManager

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

    @classmethod
    def create_new_tourist(cls, name, family, mobile):
        cursor = DatabaseManager.get_cursor()
        cursor.execute("""INSERT INTO Tourist (Name, Family, Mobile) OUTPUT INSERTED.TouristId VALUES (?,?,?)""", name, family, mobile)
        inserted_id = int(cursor.fetchval())
        cursor.commit()
        return inserted_id