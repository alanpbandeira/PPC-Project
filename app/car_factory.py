from car import Car


class CarFactory(object):

    def __init__(self, bridge):
        self._unique_bridge = bridge

    def get_car(self, id, lane_side):
        lane = lane_side[0].upper() + lane_side[1:]

        return Car(
            name="{} Car {}".format(lane, id),
            bridge=self._unique_bridge
        )