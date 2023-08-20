USE dbLake;
CREATE TABLE Tourist (
    TouristId INT PRIMARY KEY IDENTITY(1,1) NOT NULL,
    Name NVARCHAR(20) NOT NULL,
    Family NVARCHAR(30) NOT NULL,
    Mobile NVARCHAR(11) NOT NULL,
    IsActive BIT NOT NULL
);
CREATE TABLE BoatType (
    BoatTypeId INT PRIMARY KEY IDENTITY(1,1) NOT NULL,
    BoatTypeName NVARCHAR(15) NOT NULL
);
INSERT INTO BoatType (BoatTypeName)
VALUES (?), (?), (?);
CREATE TABLE Boat (
    BoatId INT PRIMARY KEY IDENTITY(1,1) NOT NULL,
    BoatTypeId INT NOT NULL,
    Color NVARCHAR(15) NOT NULL,
    OwnerId INT NOT NULL,
    PassengerCount INT NOT NULL,
    BodyStatus BIT NOT NULL,
    FullFuel BIT NULL,
    PaddleCount INT NULL,
    PedalStatus BIT NULL,
    IsActive BIT NOT NULL,
    CONSTRAINT FK_Boat_BoatType FOREIGN KEY (BoatTypeId) REFERENCES BoatType(BoatTypeId),
    CONSTRAINT FK_Boat_Owner FOREIGN KEY (OwnerId) REFERENCES Tourist(TouristId)
);
CREATE TABLE Rent (
    RentId INT PRIMARY KEY IDENTITY(1,1) NOT NULL,
    BoatId INT NOT NULL,
    TouristId INT NOT NULL,
    RentTime DATETIME NOT NULL,
    ReturnTime DATETIME NULL,
    OwnerIncome INT NULL,
    LakeIncome INT NULL,
    CONSTRAINT FK_Rent_Boat FOREIGN KEY (BoatId) REFERENCES Boat(BoatId),
    CONSTRAINT FK_Rent_Tourist FOREIGN KEY (TouristId) REFERENCES Tourist(TouristId)
);