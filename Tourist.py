from DatabaseManager import DatabaseManager
from MotorBoat import MotorBoat
from PedalBoat import PedalBoat
from RowBoat import RowBoat
from Boat import Boat

class Tourist:
    def __init__(self, tourist_id: int = 0,
                 name: str = "",
                 family: str = "",
                 mobile: str = "",
                 boat_list: list[Boat] = []):
        self.tourist_id = tourist_id
        self.name = name
        self.family = family
        self.mobile = mobile
        self.boat_list = boat_list

    @classmethod
    def create_new_tourist(cls, name, family, mobile) -> int:
        cursor = DatabaseManager.get_cursor()
        cursor.execute("""INSERT INTO Tourist (Name, Family, Mobile) OUTPUT INSERTED.TouristId VALUES (?,?,?)""", name, family, mobile)
        inserted_id = int(cursor.fetchval())
        cursor.commit()
        return inserted_id
    
    @classmethod
    def edit_tourist_info(cls, tourist_id, name, family, mobile):
        cursor = DatabaseManager.get_cursor()
        cursor.execute("""UPDATE Tourist SET Name = ?, Family = ?, Mobile = ? WHERE TouristId = ?""",
                       name, family, mobile, tourist_id)
        cursor.commit()

    @classmethod
    def get_all_tourists_id(cls) -> list[int]:
        cursor = DatabaseManager.get_cursor()
        cursor.execute("SELECT TouristId FROM Tourist")
        return [int(row[0]) for row in cursor]
    
    @classmethod
    def get_tourist_by_id(cls, tourist_id) -> 'Tourist':
        cursor = DatabaseManager.get_cursor()
        cursor.execute("""SELECT T.Name, T.Family, T.Mobile, B.BoatId, BT.BoatTypeName
                       FROM Tourist AS T
                       LEFT JOIN Boat AS B ON T.TouristId = B.OwnerId
                       LEFT JOIN BoatType AS BT ON B.BoatTypeId = BT.BoatTypeId
                       WHERE TouristId = ?""",
                       tourist_id)
        items = cursor.fetchall()
        name = items[0][0]
        family = items[0][1]
        mobile = items[0][2]

        boats = []
        for item in items:
            if item[4] == 'موتوری':
                boats.append(MotorBoat(boat_id=int(item[3])))
            elif item[4] == 'پدالی':
                boats.append(PedalBoat(boat_id=int(item[3])))
            elif item[4] == 'پارویی':
                boats.append(RowBoat(boat_id=int(item[3])))
        return Tourist(tourist_id, name, family, mobile, boats)