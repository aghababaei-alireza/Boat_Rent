from MotorBoat import MotorBoat
from PedalBoat import PedalBoat
from RowBoat import RowBoat
from Tourist import Tourist
from Rent import Rent
from DatabaseManager import DatabaseManager

cursor = DatabaseManager.get_cursor()
cursor.execute("""SELECT b.BoatId, bt.BoatTypeName, b.Color, b.OwnerId, b.PassengerCount, b.BodyStatus, b.FullFuel, b.PaddleCount, b.PedalStatus 
                       FROM Boat AS b
                       INNER JOIN BoatType AS bt ON b.BoatTypeId = bt.BoatTypeId WHERE b.BoatId = ?""", 2)

