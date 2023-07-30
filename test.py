# import pyodbc

# connection_string = "DRIVER={SQL SERVER};SERVER=localhost;DATABASE=dbLake;TRUSTED_CONNECTION=yes;"
# conn = pyodbc.connect(connection_string, encoding="utf-8")
# cursor = conn.cursor()
# cursor.execute("SELECT Mobile FROM Tourist WHERE TouristId = 1")
# print(type(cursor.fetchval()))


# cursor.fetchall() # [(1,'ali','mohammadi','0912356487'), (2, 'reza', 'akbari', '0912564389')]
# cursor.fetchone() # (1,'ali','mohammadi','0912356487')
# cursor.fetchval() # 'ali'



from MotorBoat import MotorBoat
from Tourist import Tourist
from Rent import Rent
from datetime import datetime

boat = MotorBoat(1, "white", 1, 4, True, True)
tourist = Tourist(1, "Ali", "Akbari", "0912365478")
rent = Rent(1, boat, tourist, datetime(2023,7,29))

print(rent.boat.owner_id)
print(rent.tourist.tourist_id)

Tourist.create_new_tourist()