

class Car(object):

    def __init__(self, name, lane_side, bridge_flag):
        self.bridge_flag = bridge_flag
        self._lane_side = lane_side
        self._name = name

    def __call__(self):
        self.bridge_flag.cross_bridge(self)
    
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
