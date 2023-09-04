from Core import *

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
        cursor.execute("""INSERT INTO Tourist (Name, Family, Mobile, IsActive) OUTPUT INSERTED.TouristId VALUES (?,?,?,1)""", name, family, mobile)
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
    def delete_tourist(cls, tourist_id):
        cursor = DatabaseManager.get_cursor()
        cursor.execute("""UPDATE Tourist SET IsActive = 0 WHERE TouristId = ?""", tourist_id)
        cursor.commit()
        Boat.delete_tourist_boats(tourist_id)
    
    @classmethod
    def get_all_tourists_id(cls) -> list[int]:
        cursor = DatabaseManager.get_cursor()
        cursor.execute("SELECT TouristId FROM Tourist WHERE IsActive = 1")
        return [int(row[0]) for row in cursor]
    
    @classmethod
    def get_all_tourists(cls) -> list['Tourist']:
        cursor = DatabaseManager.get_cursor()
        cursor.execute("SELECT TouristId, Name, Family, Mobile FROM Tourist WHERE IsActive = 1")
        tourists = []
        for row in cursor:
            tourist_id = int(row[0])
            name = row[1]
            family = row[2]
            mobile = row[3]
            tourists.append(Tourist(tourist_id, name, family, mobile))
        return tourists
    
    @classmethod
    def get_tourist_by_id(cls, tourist_id) -> 'Tourist':
        cursor = DatabaseManager.get_cursor()
        cursor.execute("""SELECT T.Name, T.Family, T.Mobile, B.BoatId, BT.BoatTypeName
                       FROM Tourist AS T
                       LEFT JOIN Boat AS B ON T.TouristId = B.OwnerId
                       LEFT JOIN BoatType AS BT ON B.BoatTypeId = BT.BoatTypeId
                       WHERE T.TouristId = ? AND T.IsActive = 1""",
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
    
    @classmethod
    def is_tourist_available(cls, tourist_id: int):
        cursor = DatabaseManager.get_cursor()
        cursor.execute("""SELECT * FROM Tourist AS T
                       INNER JOIN Rent AS R ON T.TouristId = R.TouristId
                       WHERE T.TouristId = ? AND R.ReturnTime IS NULL""",
                       tourist_id)
        return not cursor.fetchval()
