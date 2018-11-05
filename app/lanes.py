from threading import Thread
import threading
import time
import numpy as np


class Lane(Thread):

    _MAX_CARS = 50

    def __init__(self, side, car_factory):
        super(Lane, self).__init__()
        self._cars = []
        self.car_factory = car_factory
        self.side = side
        self.arrived_count = 0
        self.delta_arrival = 4

    def car_arrival(self, delta_time):
        if delta_time > 2:
            prob_range = (100 / self.delta_arrival) * delta_time / 100
            run_chance = np.random.rand()
            if run_chance <= prob_range:
                car_id=len(self._cars) + 1
                
                new_car = self.car_factory.get_car(
                    id=car_id, lane_side=self.side
                )
                self._cars.append(new_car)
                self.arrived_count += 1

                return True
        
        return False
                
    def run(self):
        # initiate current time
        previous_time = time.time()
        # initiate previous time

        while self.arrived_count < self._MAX_CARS:
            current_time = time.time()
            delta_time = int(current_time - previous_time)
            if self.car_arrival(delta_time):
                self.arrived_count += 1
                previous_time = current_time
            
            if len(self._cars) > 0:
                car = self._cars.pop()
                new_thread = Thread(target=car)
                new_thread.start()
                new_thread.join()
