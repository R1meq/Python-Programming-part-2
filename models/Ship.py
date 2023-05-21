from abc import ABC, abstractmethod


class Ship(ABC):

    def __init__(self, id, name, captain, current_port, max_speed, max_capacity,
                 current_load, current_speed, crew_count, support_stuff):
        self.id = id
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
        pass

    @abstractmethod
    def calculate_load_time(self) -> float:
        pass
