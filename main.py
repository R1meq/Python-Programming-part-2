"""import container ship"""
from models.container_ship import ContainerShip


if __name__ == "__main__":
    new_ship = ContainerShip(18.7, "ContainerShip 2",
                             "Tom Cruise", "Shanghai", 17.7, 110.5, 100,
                             15.6, 27, 45, 2.5, "foodstuffs", 20)

    new_ship.load_cargo(20)
