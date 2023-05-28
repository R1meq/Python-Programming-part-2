"""A class that manages ships"""
from functools import wraps

from decorator.decorator import log_arguments_to_file, to_tuple


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
    @to_tuple
    def find_all_ships_with_current_load_more_than(self, current_load):
        """
        Finds and returns a list of ships with a current load greater than the specified value.
        :param current_load:the maximum current load of the ship
        :return:A list of ships with a current load greater than the specified value.
        """
        return list(filter(lambda a: a.current_load > current_load, self.ships))

    def __len__(self):
        return len(self.ships)

    def __getitem__(self, item):
        return self.ships[item]

    def __iter__(self):
        return self

    @log_arguments_to_file
    def get_result_of_calculate_load_time(self):
        return [f"load time: {ship.calculate_load_time()}" for ship in self.ships]


    def enumerating(self):
        for index, ship in enumerate(self.ships):
            print(f"{index}: {ship}")

    def zipping(self):
        for obj, result in zip(self.ships, self.get_result_of_calculate_load_time()):
            print(f"{obj}: {result}")

    def if_any_ship_has_weight_over(self, current_load):
        return any(ship.current_load >= current_load for ship in self.ships)

    def if_all_ship_has_weight_over_50(self, current_load):
        return all(ship.current_load >= current_load for ship in self.ships)



