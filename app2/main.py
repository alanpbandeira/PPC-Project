from car_factory import CarFactory
from bridge_flag import BridgeFlag
from lanes import Lane

flag = BridgeFlag()

factory = CarFactory(flag)

# left_lane = Lane(side='left', car_factory=factory, daemon=True)
# right_lane = Lane(side='right', car_factory=factory, daemon=True)

producer = Lane(car_factory=factory)
producer.start()
producer.join()

# left_lane.start()
# right_lane.start()

# left_lane.join()
# right_lane.join()

print("Exiting main thread")