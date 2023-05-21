class ShipManager:
    ships = []

    def add_ship(self, ship):
        self.ships.append(ship)

    def find_all_ships_with_capacity_more_than(self, max_capacity):
        return [ship for ship in self.ships if ship.max_capacity > max_capacity]

    def find_all_ships_with_current_load_more_than(self, current_load):
        return [ship for ship in self.ships if ship.current_load > current_load]