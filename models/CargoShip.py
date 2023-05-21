from abc import ABC

from models.Ship import Ship


class CargoShip(Ship, ABC):
    """
     A base abstract class representing a cargo ship.

    Attributes:
        id (int): The unique identifier of the ship.
        name (str): The name of the ship.
        captain (str): The name of the ship's captain.
        current_port (str): The current port where the ship is located.
        max_speed (float): The maximum speed of the ship.
        max_capacity (float): The maximum cargo capacity of the ship.
        current_load (float): The current cargo load of the ship.
        current_speed (float): The current speed of the ship.
        crew_count (int): The number of crew members on the ship.
        support_staff (int): The number of support staff members on the ship.
        tonnage (float): The tonnage of the cargo ship.
        type_of_cargo (str): The type of cargo the cargo ship carries.
    """

    MINUTES_IN_HOUR = 60
    AVERAGE_LOAD_TIME = 20

    def __init__(self, id, name, captain, current_port, max_speed,
                 max_capacity, current_load, current_speed, crew_count,
                 support_stuff, tonnage, type_of_cargo):
        super().__init__(id, name, captain, current_port, max_speed,
                         max_capacity, current_load, current_speed,
                         crew_count, support_stuff)
        self.tonnage = tonnage
        self.type_of_cargo = type_of_cargo
