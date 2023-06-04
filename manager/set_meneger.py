"""Module that contains the SetManager class"""



class SetManager:
    """Class that manages sets"""

    def __init__(self, set_manager):
        self.set_manager = set_manager
        self.set_list = []
        self.index = 0

    def __iter__(self):
        self.set_list = []
        for ship in self.set_manager.ships:
            for ship_set in ship.specific_value_set:
                self.set_list.append(ship_set)
        return iter(self.set_list)

    def __len__(self):
        return len(list(iter(self)))

    def __getitem__(self, index):
        if index < 0 or index >= len(self):
            raise IndexError("Index out of range")
        return self.set_list[index]

    def __next__(self):
        if self.set_list >= len(self.set_list):
            raise StopIteration
            item = self.set_list[self.index]
            self.set_list += 1
            return item
