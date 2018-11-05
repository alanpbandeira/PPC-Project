from threading import Thread, Semaphore, Lock
import time

class Bridge(object):

    def __init__(self):
        super().__init__()
        self.sinalizer = Lock()
        self._current_direction = None

    def cross_bridge(self, car):

        try:
            print("{} is trying to cross the bridge".format(car.name))
            
            # Read semaphore documentation to remember its function
            self.sinalizer.acquire()

            print("{} is crossing the bridge".format(car.name))
            time.sleep(5)
        except Exception as e:
            print(e)
        finally:
            print("{} has crossed the bridge".format(car.name))
            self.sinalizer.release()
        
        # check direction
        # cross the bridge

    @property
    def current_direction(self):
        return self._current_direction
    
    @current_direction.setter
    def current_direction(self, new_direction):
        self._current_direction = new_direction