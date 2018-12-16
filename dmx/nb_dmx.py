from dmx import set_dmx, blackout


class rgb_can():

    def __init__(self, id, channels):
        self.channels = channels  # {obj, address} e.g. {red, 61}
        self.id = id
        self.lights = self.make_lights()

    def make_lights(self):
        return {addr: 0 for _, addr in self.channels.items()}

    def _set_obj_value(self, obj, value):
        if obj in self.channels:
            addr = self.channels[obj]
            self.lights[addr] = value
            return True
        else:
            return False

    def _get_obj_power(self, obj):
        if obj in self.channels:
            return self.channels[obj]

    def set_power(self, val):
        self._set_obj_power('power', val)

    def get_power(self):
        return self._get_obj_power('power')

    power = property(get_power, set_power)

    def set_value(self, val):
        self._set_obj_value('value', val)

    def get_value(self):
        return self._get_obj_value('value')

    value = property(get_value, set_value)

    def set_red(self, val):
        self._set_obj_value('red', val)

    def get_red(self):
        return self._get_obj_value('red')

    red = property(get_red, set_red)

    def set_green(self, val):
        self._set_obj_value('green', val)

    def get_green(self):
        return self._get_obj_value('green')

    green = property(get_green, set_green)

    def set_blue(self, val):
        self._set_obj_value('blue', val)

    def get_blue(self):
        return self._get_obj_value('blue')

    blue = property(get_blue, set_blue)

    def set_pattern(self, val):
        self._set_obj_value('pattern', val)

    def get_pattern(self):
        return self._get_obj_value('pattern')

    pattern = property(get_pattern, set_pattern)
