from car_factory import CarFactory
from bridge_flag import BridgeFlag
from lanes import Lane

flag = BridgeFlag()

factory = CarFactory(flag)

producer = Lane(car_factory=factory)
producer.start()
producer.join()

print("Exiting main thread")