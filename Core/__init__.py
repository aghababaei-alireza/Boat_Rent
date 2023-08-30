from abc import ABC
import pyodbc
from datetime import datetime
from math import ceil

from Core.DatabaseManager import DatabaseManager
from Core.Boat import Boat, MotorBoat, PedalBoat, RowBoat
from Core.Tourist import Tourist
from Core.Rent import Rent