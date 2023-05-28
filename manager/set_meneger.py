"""Module that contains the SetManager class"""
from models import ship


class SetManager:
    """Class that manages sets"""

    def __init__(self, set_manager):
        self.set_manager = set_manager

    def __iter__(self):
        for ship in self.set_manager.ships:
            yield from ship

    def __len__(self):
        length = 0
        for ship in self.set_manager.ships:
            length += len(ship.specific_value_set)
        return length

    def __getitem__(self, index):
        return list(self.__iter__())[index]
