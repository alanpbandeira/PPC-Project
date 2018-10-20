import time

from abc import ABC, abstractclassmethod


class Automobile(ABC):
    
    tc = 10

    @abstractclassmethod
    def cross_bridge(self):
        raise NotImplementedError

class Car(object):
    
    def __init__(self):
        pass

    def cross_bridge(self):
        pass