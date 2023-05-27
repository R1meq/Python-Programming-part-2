"""class inherited abstract class Cargo Ship"""
from models.cargo_ship import CargoShip


class TankerShip(CargoShip):

    """
     A class representing a tanker ship

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
        tonnage (float): The tonnage of the tanker ship.
        type_of_cargo (str): The type of cargo the tanker ship carries.
        volume_in_barrels (float): The volume of cargo in barrels.
    """

    def __init__(self, ship_id, name, captain, current_port, max_speed,
                 max_capacity, current_load, current_speed, crew_count,
                 support_stuff, tonnage, type_of_cargo, volume_in_barrels):
        super().__init__(ship_id, name, captain, current_port,
                         max_speed, max_capacity, current_load,
                         current_speed, crew_count,
                         support_stuff, tonnage, type_of_cargo)
        self.volume_in_barrels = volume_in_barrels

    def get_total_people_count(self) -> int:
        """
        :returns: The total number of people on the tanker ship.
        """
        return self.crew_count + self.support_stuff

    def calculate_load_time(self) -> float:
        """
        :returns: The estimated time to load the cargo on the tanker ship.
        """
        return self.MINUTES_IN_HOUR * self.tonnage / self.AVERAGE_LOAD_TIME

    def __str__(self):
        return f"TankerShip: id={self.id}, " \
               f"name={self.name}, " \
               f"captain={self.captain}, " \
               f"current_port={self.current_port}, " \
               f"max_speed={self.max_speed}, " \
               f"max_capacity={self.max_capacity}, " \
               f"current_load={self.current_load}, " \
               f"current_speed={self.current_speed}, " \
               f"crew_count={self.crew_count}, " \
               f"support_stuff={self.support_stuff}, " \
               f"tonnage={self.tonnage}, " \
               f"type_of_cargo={self.type_of_cargo}, " \
               f"volume_in_barrels={self.volume_in_barrels}"
