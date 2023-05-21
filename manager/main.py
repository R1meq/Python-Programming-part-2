from manager.ShipManager import ShipManager
from models.ContainerShip import ContainerShip
from models.CruiseShip import CruiseShip
from models.RoroShip import RoroShip
from models.TankerShip import TankerShip

manager = ShipManager()
manager.add_ship(TankerShip(20.4, "TankerShip 1",
                            "Mike Shinoda", "Odessa", 13.5, 50.2, 40.2,
                            11.5, 15, 28, 44.5,10.6, "gasoline"))

manager.add_ship(TankerShip(10.5, "TankerShip 2",
                            "Joe Hahn", "Lisbon", 15.6, 60.2, 20.6,
                            13.6, 20, 36, 65.7,16.9, "crude oil"))

manager.add_ship(RoroShip(11.6, "ROROShip 1",
                          " Brad Delson", "LA", 18.6, 15.6, 12.5,
                          16.6, 17, 21, 15.2, "cars", 20))

manager.add_ship(RoroShip(12.7, "ROROShip 2",
                          " Dave Farrell", "Boston", 22, 25.6, 23.6,
                          21, 18, 22, 15.2, "trucks", 20))

manager.add_ship(ContainerShip(15.6, "ContainerShip 1",
                               "Rob Bourdon", "Lviv", 19.5, 125, 102,
                               18.5, 20, 35,2.5, "raw materials", 20))

manager.add_ship(ContainerShip(18.7, "ContainerShip 2",
                               "Tom Cruise", "Shanghai", 17.7, 110.5, 65,
                               15.6, 27, 45, 2.5, "foodstuffs", 20))

manager.add_ship(CruiseShip(10.2, "CruiseShip 1",
                            "Cristiano Ronaldo", "Hong Kong", 21.6, 76.5, 76.5,
                            16.7, 60, 30, 150))

manager.add_ship(CruiseShip(10.6, "CruiseShip 2",
                            "Mr Beast", "Singapore", 24.0, 100, 80,
                            23.0, 45, 36, 200))

for ship in manager.ships:
    print(ship)

print("========================")

for ship in manager.find_all_ships_with_capacity_more_than(50.2):
    print(ship.__str__())

print("========================")

for ship in manager.find_all_ships_with_current_load_more_than(65.5):
    print(ship.__str__())

