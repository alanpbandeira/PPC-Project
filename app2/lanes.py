from threading import Thread

import time
import numpy as np


class Lane(Thread):

    _MAX_CARS = 50
    _MAX_TRUCKS = 3
    _CAR_TYPE = ['C', 'T']

    def __init__(self, car_factory, daemon=False):
        super(Lane, self).__init__(daemon=daemon)
        self._cars = []
        self.car_factory = car_factory
        self.cars_left = 0
        self.cars_right = 0
        self.trucks_left = 0
        self.trucks_right = 0
        self.delta_arrival = 4

    def car_arrival(self, delta_time):
        """
        Check elapsed time and if enough time has passed spam a new car based on
        a probability.
        :param delta_time:
        :return boolean:
        """

        if delta_time > 2:
            prob_range = (100 / self.delta_arrival) * delta_time / 100
            run_chance = np.random.rand()

            if run_chance <= prob_range:

                # Check if sides are available
                if self.cars_left == self._MAX_CARS:
                    side = 'right'
                elif self.cars_right == self._MAX_CARS:
                    side = 'left'
                else:
                    side = np.random.choice(['left', 'right'])

                if side == 'right':
                    car_id = self.cars_right + 1
                    self.cars_right += 1
                else:
                    car_id = self.cars_left + 1
                    self.cars_left += 1

                new_car = self.car_factory.get_car(
                    id=car_id, lane_side=side
                )

                self._cars.append(new_car)

                return True
        
        return False
                
    def run(self):
        """
        Overriding the run method of the Thread superclass
        :return:
        """

        # Get initial time
        initial_time = time.time()

        # Working control flags
        arriving = True
        empty = True

        while True:

            if arriving:
                # Get current time
                current_time = time.time()

                # Calculate elapsed time
                delta_time = int(current_time - initial_time)

                # If new car arrives reset elapsed time
                if self.car_arrival(delta_time):
                    initial_time = current_time
                    empty = False

                # Finish cars arrival
                full_right = self.cars_right == self._MAX_CARS
                full_left = self.cars_left == self._MAX_CARS

                if full_right and full_left:
                    arriving = False

            # If cars on the lane, let the first car
            # in the queue try to cross the bridge
            if not empty:
                # time.sleep(2)
                car = self._cars.pop()
                new_thread = Thread(target=car, daemon=True)
                new_thread.start()
                # new_thread.join()

            # Signal empty lane avoiding attempts to spam new cars
            if not self._cars:
                empty = True

            # If all cars arrived and are
            # crossing the bridge the lane finishes
            if not arriving and empty:
                break
