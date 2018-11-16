

class Car(object):

    def __init__(self, name, lane_side, bridge_flag, car_type, traverse_time):
        self._bridge_flag = bridge_flag
        self._lane_side = lane_side
        self._name = name
        self._car_type = car_type
        self._traverse_time = traverse_time

    def __call__(self):
        self._bridge_flag.cross_bridge(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def lane_side(self):
        return self._lane_side

    @lane_side.setter
    def lane_side(self, new_side):
        self._lane_side = new_side

    @property
    def car_type(self):
        return self._car_type

    @car_type.setter
    def car_type(self, new_type):
        self._car_type = new_type

    @property
    def traverse_time(self):
        return self._traverse_time

    @traverse_time.setter
    def traverse_time(self, new_time):
        self._traverse_time = new_time