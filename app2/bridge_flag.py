from threading import Semaphore,Lock, Condition
import numpy as np
import time


class BridgeFlag(object):

    SIDES = ['left', 'right']

    def __init__(self):
        super().__init__()
        self.semaphore = Semaphore(value=5)
        self.condition_cross = Condition()
        self._current_direction = np.random.choice(self.SIDES)
        self.right_crossed = 0
        self.left_crossed = 0

    def check_side(self, car_side):
        return car_side == self._current_direction

    def cross_bridge(self, car):
        """docstring"""

        crossed = False

        while not crossed:
                try:
                    print("{} is trying to cross the bridge".format(car.name))

                    with self.condition_cross:
                        while self._current_direction != car.lane_side:
                            print(self._current_direction, car.lane_side)

                            print(car.name + ' is gonna wait')
                            self.condition_cross.wait()
                            print(car.name + ' was notified')

                            # tries to flip the signal if no one is crossing
                            if self.semaphore._value == 0:
                                self.revert_signal()
                                self.right_crossed = self.left_crossed = 0

                        # time.sleep(2)
                        self.semaphore.acquire()
                        print("{} is crossing the bridge".format(car.name))
                        time.sleep(10)
                        print("{} has crossed the bridge".format(car.name))
                        crossed = True

                        if self._current_direction == self.SIDES[0]:
                            self.left_crossed += 1
                            self.right_crossed = 0
                        else:
                            self.right_crossed += 1
                            self.left_crossed = 0

                        if self.right_crossed == 5 or self.left_crossed == 5:
                            self.revert_signal()
                            self.right_crossed = self.left_crossed = 0
                            self.condition_cross.notify_all()

                        self.semaphore.release()
                        self.condition_cross.notify_all()

                except Exception as e:
                    print(e)

    def revert_signal(self):
        idx = self.SIDES.index(self._current_direction) - 1
        self._current_direction = self.SIDES[idx]
        print('direction changed')

    @property
    def current_direction(self):
        return self._current_direction

    @current_direction.setter
    def current_direction(self, new_direction):
        self._current_direction = new_direction
