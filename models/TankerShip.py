from models.CargoShip import CargoShip


class TankerShip(CargoShip):

    def __init__(self, id, name, captain, current_port, max_speed,
                 max_capacity,current_load, current_speed, crew_count,
                 support_stuff, tonnage, type_of_cargo, volume_in_barrels):
        super().__init__(id, name, captain, current_port, max_speed,
                         max_capacity, current_load, current_speed, crew_count,
                         support_stuff, tonnage, type_of_cargo)
        self.volume_in_barrels = volume_in_barrels

    def get_total_people_count(self) -> int:
        return self.crew_count + self.support_stuff

    def calculate_load_time(self) -> float:
        return self.MINUTES_IN_HOUR * self.tonnage / self.AVERAGE_LOAD_TIME

    def __str__(self):
        return f"TankerShip: id={self.id}, name={self.name}, captain={self.captain}," \
               f"current_port={self.current_port}, max_speed={self.max_speed}," \
               f"max_capacity={self.max_capacity}, current_load={self.current_load}," \
               f"current_speed={self.current_speed}, crew_count={self.crew_count}" \
               f"support_stuff={self.support_stuff}, tonnage={self.tonnage}," \
               f" type_of_cargo={self.type_of_cargo}, volume_in_barrels={self.volume_in_barrels}"
