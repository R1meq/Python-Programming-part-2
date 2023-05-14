class Ship:

    instance = None

    def __init__(self, id=0.0, name="", captain="", current_port="", max_speed=0.0, max_capacity=0.0,
                 current_load=0.0, current_speed=0.0):
        self.__id = id
        self.__name = name
        self.__captain = captain
        self.__current_port = current_port
        self.__max_speed = max_speed
        self.__max_capacity = max_capacity
        self.__current_load = current_load
        self.__current_speed = current_speed

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def captain(self):
        return self.__captain

    @property
    def current_port(self):
        return self.__current_port

    @property
    def max_speed(self):
        return self.__max_speed

    @property
    def max_capacity(self):
        return self.__max_capacity

    @property
    def current_load(self):
        return self.__current_load

    @property
    def current_speed(self):
        return self.__current_speed

    @id.setter
    def id(self, id):
        self.__id = id

    @name.setter
    def name(self, name):
        self.__name = name

    @captain.setter
    def captain(self, captain):
        self.__captain = captain

    @current_port.setter
    def current_port(self, current_port):
        self.__current_port = current_port

    @max_speed.setter
    def max_speed(self, max_speed):
        self.__max_speed = max_speed

    @max_capacity.setter
    def max_capacity(self, max_capacity):
        self.__max_capacity = max_capacity

    @current_load.setter
    def current_load(self, current_load):
        self.__current_load = current_load

    @current_speed.setter
    def current_speed(self, current_speed):
        self.__current_speed = current_speed


    def __str__(self):
        return f"Ship:( \
               id={self.__id},\
               name={self.__name},\
               captain={self.__captain},\
               current_port={self.__current_port},\
               max_speed={self.__max_speed},\
               max_capacity={self.__max_capacity},\
               current_load={self.__current_load},\
               current_speed={self.__current_speed})"

    def dock(self, port):
        self.__current_port = port
        return self.__current_port

    def set_speed(self, speed):
        if speed >= 0.0:
            self.__current_speed = speed

    def load(self, weight):
        if weight + self.__current_load <= self.__max_capacity:
            self.__current_load += weight
        else:
            self.__current_load = self.__max_capacity

    def unload(self, weight):
        if self.__current_load - weight >= 0.0:
            self.__current_load -= weight
        else:
            self.__current_load = 0.0

    @staticmethod
    def get_instance():
        if Ship.instance is None:
            Ship.instance = Ship()
        return Ship.instance
