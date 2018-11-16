from car import Car


class CarFactory(object):

    def __init__(self, bridge_flag):
        self._unique_flag = bridge_flag

    def get_car(self, id, lane_side, car_type):
        lane = lane_side[0].upper() + lane_side[1:]

        if car_type == 'C':
            traverse_time = 10
            name = "{} Car {}".format(lane, id)
        else:
            traverse_time = 20
            name = "{} Truck {}".format(lane, id)

        return Car(
            name=name,
            lane_side=lane_side,
            bridge_flag=self._unique_flag,
            car_type=car_type,
            traverse_time=traverse_time
        )

    @property
    def unique_flag(self):
        return self._unique_flag

    @unique_flag.setter
    def unique_flag(self, new_flag):
        self._unique_flag = new_flag
