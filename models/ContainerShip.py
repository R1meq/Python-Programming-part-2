from models.CargoShip import CargoShip


class ContainerShip(CargoShip):
    """
        A class representing a container ship

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
            tonnage (float): The tonnage of the container ship.
            type_of_cargo (str): The type of cargo the container ship carries.
            containers (int): The numbers of containers carried by the container ship.
        """
    def __init__(self, id, name, captain, current_port, max_speed,
                 max_capacity,current_load, current_speed, crew_count,
                 support_stuff, tonnage, type_of_cargo, containers):

        super().__init__(id, name, captain, current_port, max_speed,
                         max_capacity, current_load, current_speed,
                         crew_count, support_stuff, tonnage, type_of_cargo)
        self.containers = containers

    def calculate_load_time(self) -> float:
        """
        :return:The estimated time to load the cargo on the container ship.
        """
        return self.crew_count + self.support_stuff

    def get_total_people_count(self) -> int:
        """
        :return:The total number of people on the container ship.
        """
        return self.MINUTES_IN_HOUR * self.tonnage / self.AVERAGE_LOAD_TIME

    def __str__(self) -> str:
        return f"ContainerShip: id={self.id}, " \
               f"name={self.name}, " \
               f"captain={self.captain}, " \
               f"current_port={self.current_port}, " \
               f"max_speed={self.max_speed}, "\
               f"max_capacity={self.max_capacity}, " \
               f"current_load={self.current_load}, "\
               f"current_speed={self.current_speed}, " \
               f"crew_count={self.crew_count}, " \
               f"support_stuff={self.support_stuff}, " \
               f"tonnage={self.tonnage}, " \
               f"type_of_cargo={self.type_of_cargo}, " \
               f"containers={self.containers}"
