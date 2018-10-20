from abc import ABC, abstractclassmethod


class Lane(ABC):

    MAX_CARS = 50
    car_count = 0
    _cars = []
    
    def __len__(self):
        return len(self._cars)
    
    def __getitem__(self, position):
        return self._cars[position]

class LeftLane(Lane):
    
    def __init__(self):
        self.side = 'left'

class RightLane(Lane):
    
    def __init__(self):
        self.side = 'right'