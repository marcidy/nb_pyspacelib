from pyspacelib.dmx.dmx import (
    dmxUniverse,
    rgbCan,
    rgbSpot,
)
from pyspacelib.dmx.dmx_profiles import (
    STAGE_LEFT,
    STAGE_RIGHT,
    DISCO,
    RGB_CAN_PROFILE,
    RGB_SPOT_PROFILE,
)


universe = dmxUniverse(1)


def create_fixtures(universe):
    can_ids = list(STAGE_LEFT.values()) + list(STAGE_RIGHT.values())
    cans = [rgbCan(id, RGB_SPOT_PROFILE) for id in can_ids]
    spots = [rgbSpot(id, RGB_SPOT_PROFILE) for id in DISCO.values()]

    [universe.add_fixture(can) for can in cans]
    [universe.add_fixture(spot) for spot in spots]

    return universe


universe = create_fixtures(universe)

__all__ = [rgbCan,
           rgbSpot,
           dmxUniverse]
