from abc import ABC

from models.Ship import Ship


class CargoShip(Ship, ABC):
    MINUTES_IN_HOUR = 60
    AVERAGE_LOAD_TIME = 20

    def __init__(self, id, name, captain, current_port, max_speed,
                 max_capacity,current_load, current_speed, crew_count,
                 support_stuff, tonnage, type_of_cargo):
        super().__init__(id, name, captain, current_port, max_speed,
                         max_capacity, current_load, current_speed,
                         crew_count, support_stuff)
        self.tonnage = tonnage
        self.type_of_cargo = type_of_cargo
