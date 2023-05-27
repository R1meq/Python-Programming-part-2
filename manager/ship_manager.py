"""A class that manages ships"""


class ShipManager:
    """
    A class that manages ships

    Attributes:
        ships (list): A list of ships.
    """
    def __init__(self):
        self.ships = []

    def add_ship(self, ship):
        """
        Adds a ship to the list of ships.
        :param ship: ship to add
        :return: None
        """
        self.ships.append(ship)

    def find_all_ships_with_capacity_more_than(self, max_capacity):
        """
        Finds and returns a list of ships with a maximum capacity greater than the specified value.
        :param max_capacity: the maximum capacity of the ship
        :return:A list of ships with a maximum capacity greater than the specified value.
        """
        return list(filter(lambda a: a.max_capacity > max_capacity, self.ships))

    def find_all_ships_with_current_load_more_than(self, current_load):
        """
        Finds and returns a list of ships with a current load greater than the specified value.
        :param current_load:the maximum current load of the ship
        :return:A list of ships with a current load greater than the specified value.
        """
        return list(filter(lambda a: a.current_load > current_load, self.ships))