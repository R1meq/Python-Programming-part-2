"""class inherited abstract class Ship"""
from models.ship import Ship


class CruiseShip(Ship):
    """
    A class representing a cruise ship

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
        passenger_count (int): The number of passengers on the cruise ship.
    """
    AVERAGE_LOAD_TIME_FOR_PASSENGER = 5

    def __init__(self, ship_id, name, captain, current_port, max_speed,
                 max_capacity, current_load, current_speed, crew_count,
                 support_stuff, passenger_count):
        super().__init__(ship_id, name, captain, current_port, max_speed,
                         max_capacity, current_load, current_speed,
                         crew_count, support_stuff)
        self.passenger_count = passenger_count

    def __str__(self):
        return f"CruiseShip: id={self.id}, " \
               f"name={self.name}, " \
               f"captain={self.captain}, " \
               f"current_port={self.current_port}, " \
               f"max_speed={self.max_speed}, " \
               f"max_capacity={self.max_capacity}, " \
               f"current_load={self.current_load}, " \
               f"current_speed={self.current_speed}, " \
               f"passenger_count={self.passenger_count}"

    def calculate_load_time(self) -> int:
        """
        :return: The estimated time to load the passengers on the cruise ship.
        """
        return self.passenger_count * self.AVERAGE_LOAD_TIME_FOR_PASSENGER

    def get_total_people_count(self) -> int:
        """
        :return:The total number of people on the cruise ship.
        """
        return self.passenger_count + self.crew_count + self.support_stuff
