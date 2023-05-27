"""class inherited abstract class ABC"""
from abc import ABC, abstractmethod


class Ship(ABC):
    """
    A base abstract class representing a ship.

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
    """

    def __init__(self, ship_id, name, captain, current_port,
                 max_speed, max_capacity, current_load,
                 current_speed, crew_count, support_stuff):
        self.id = ship_id
        self.name = name
        self.captain = captain
        self.current_port = current_port
        self.max_speed = max_speed
        self.max_capacity = max_capacity
        self.current_load = current_load
        self.current_speed = current_speed
        self.crew_count = crew_count
        self.support_stuff = support_stuff

    @abstractmethod
    def get_total_people_count(self) -> int:
        """
        :returns:number of people on the ship (crew count + support staff).
        """

    @abstractmethod
    def calculate_load_time(self) -> float:
        """
        :returns:The estimated time to load the cargo on the ship.
        """
