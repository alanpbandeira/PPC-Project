from car import Car


class CarFactory(object):

    def __init__(self, bridge_flag):
        self._unique_flag = bridge_flag

    def get_car(self, id, lane_side):
        lane = lane_side[0].upper() + lane_side[1:]

        return Car(
            name="{} Car {}".format(lane, id),
            lane_side=lane_side,
            bridge_flag=self._unique_flag
        )

    @property
    def unique_flag(self):
        return self._unique_flag

    @unique_flag.setter
    def unique_flag(self, new_flag):
        self._unique_flag = new_flag
