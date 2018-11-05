import numpy as np


class Car(object):

    def __init__(self, name, bridge):
        self.bridge = bridge
        self._name = name

    def __call__(self):
        self.bridge.cross_bridge(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name