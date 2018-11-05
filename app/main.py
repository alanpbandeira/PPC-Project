import numpy as np
import time
from car import Car
from bridge import Bridge
from threading import Thread

# Arrival time
# ta = np.random.randint(2, 7)

# Travessy time
# tc = 10

# Max cars through bridge, per side
# If bridge cosume fire in a row from the same side, it should switch sides
# P = 5

# Switch sides if max cars perside is reached 
# and cars in the other side are waiting

# Define vehicles
# Define One way bridge

# main loop
# while True:
#     break

#
# Implementar o uso da ponte!!
#

the_bridge = Bridge()

car_one = Car(name="Car 1", bridge=the_bridge)
car_two = Car(name="Car 2", bridge=the_bridge)

th_one = Thread(target=car_one)
th_two = Thread(target=car_two)

threads = [th_one, th_two]

th_one.start()
th_two.start()

for t in threads:
    t.join()

print("Exiting main thread")