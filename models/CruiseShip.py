from models.Ship import Ship


class CruiseShip(Ship):
    AVERAGE_LOAD_TIME_FOR_PASSENGER = 5

    def __init__(self, id, name, captain, current_port, max_speed,
                 max_capacity,current_load, current_speed, crew_count,
                 support_stuff, passenger_count):
        super().__init__(id, name, captain, current_port, max_speed,
                         max_capacity, current_load, current_speed,
                         crew_count, support_stuff)
        self.passenger_count = passenger_count

    def __str__(self):
        return f"CruiseShip: id={self.id}, name={self.name}, captain={self.captain}, " \
               f"current_port={self.current_port}, max_speed={self.max_speed}, " \
               f"max_capacity={self.max_capacity}, current_load={self.current_load}, " \
               f"current_speed={self.current_speed}, passenger_count={self.passenger_count}"

    def calculate_load_time(self) -> float:
        return self.passenger_count * self.AVERAGE_LOAD_TIME_FOR_PASSENGER

    def get_total_people_count(self) -> int:
        return self.passenger_count + self.crew_count + self.support_stuff
