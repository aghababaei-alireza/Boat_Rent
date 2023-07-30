from MotorBoat import MotorBoat
from PedalBoat import PedalBoat
from RowBoat import RowBoat
from Tourist import Tourist
from Rent import Rent
from DatabaseManager import DatabaseManager

id = Tourist.create_new_tourist("شهره", "شهسواری", "09142568739")
print(id)

id = 1
name = 'ali'
values = (id, name)
cursor.execute("""SELECT * FROM Tourist WHERE TouristId = """ + str(id))
cursor.execute(f"""SELECT * FROM Tourist WHERE TouristId = {id}""")
cursor.execute("""SELECT * FROM Tourist WHERE TouristId = ? OR Name = ?""", id, name)
cursor.execute("""SELECT * FROM Tourist WHERE TouristId = ? OR Name = ?""", values)
cursor.execute("""SELECT * FROM Tourist WHERE TouristId = ? OR Name = ?""", (id, name))