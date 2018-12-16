from requests import post
from colorsys import hsv_to_rgb

BASE = "http://10.20.1.25:9090/set_dmx"


class dmxEndPoint:

    def __init__(self, id, channels):
        self.channels = channels  # {obj, addr}
        addrs = channels.values()
        self.len = max(addrs) - min(addrs) + 1
        self.id = id
        self.values = [0]*self.len

    def __len__(self):
        return self.len

    def _set_obj_value(self, obj, value):
        if obj in self.channels:
            addr = self.channels[obj]
            self.values[addr] = value

    def _get_obj_value(self, obj):
        if obj in self.channels:
            addr = self.channels[obj]
            return self.values[addr]

    def show(self):
        return self.values


class rgbCan(dmxEndPoint):

    def set_hsv(self, h, s, v):
        r, g, b = hsv_to_rgb(h/256, s/256, v/256)
        self.set_rgb(int(r*256), int(g*256), int(b*256))

    def set_rgb(self, r=0, g=0, b=0, w=0):
        self._set_obj_value('red', r)
        self._set_obj_value('green', g)
        self._set_obj_value('blue', b)
        self._set_obj_value('white', w)

    def on(self):
        self._set_obj_value('power', 255)

    def off(self):
        self._set_obj_value('power', 0)

    def mode(self, mode):
        if mode == "solid":
            self._set_obj_value('selection', 50)
        elif mode == "change":
            self._set_obj_value("selection", 60)
        elif mode == "jump":
            self._set_obj_value("selection", 125)
        elif mode == "gradient":
            self._set_obj_value("selection", 175)
        elif mode == "pulse":
            self._set_obj_value("selection", 225)
        elif mode == "sound":
            self._set_obj_value("selection", 275)

    def speed(self, value):
        self._set_obj_value("speed", value)

    def strobe(self, speed):
        self._set_obj_value('strobe', speed)

    def set(self, object, value):
        self._set_obj_value(object, value)


class dmxUniverse:

    def __init__(self, id):
        self.id = id
        self.fixtures = {}
        self.values = 512*[0]

    def add_fixture(self, fixture):
        ''' Overwrites what was there, period '''
        self.fixtures[fixture.id] = fixture

    def push(self, operation, value):
        for fixture in self.fixtures.values():
            fixture.set(operation, value)

    def blackout(self):
        for fixture in self.fixtures.values():
            fixture.off()
        self.show()

    def all_on(self):
        for fix in self.fixtures.values():
            fix.on()

    def show(self):
        for id, fixture in self.fixtures.items():
            values = fixture.show()
            for val in range(len(values)):
                self.values[id + val-1] = values[val]

        data = {"u": str(self.id), "d": ",".join(map(str, self.values))}
        post(BASE, data=data)


class rgbSpot(dmxEndPoint):
    pass
