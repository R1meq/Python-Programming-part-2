from Ship import Ship

if __name__ == "__main__":
    ship1 = Ship()
    ship2 = Ship(12.2, "Meteora", "Mike Shinoda", "Fort Minor", 18.2, 4.5, 3.1)
    ships = [ship1, ship2, Ship.get_instance(), Ship.get_instance()]
    ships[1].load(1.2)
    ships[1].unload(2.5)

    for ship in ships:
        print(ship.__str__())
