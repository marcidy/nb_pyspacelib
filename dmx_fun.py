from dmx import dmx_profiles, dmx


def setup():
    can_ids = list(dmx_profiles.STAGE_RIGHT.values()) + \
                   list(dmx_profiles.STAGE_LEFT.values())
    spot_ids = dmx_profiles.DISCO.values()

    rgb_profile = dmx_profiles.RGB_CAN_PROFILE
    spot_profile = dmx_profiles.RGB_SPOT_PROFILE

    cans = [dmx.rgbCan(id, rgb_profile) for id in can_ids]
    spots = [dmx.rgbSpot(id, spot_profile) for id in spot_ids]

    uni = dmx.dmxUniverse(1)
    [uni.add_fixture(can) for can in cans]
    [uni.add_fixture(spot) for spot in spots]

    return uni


def parry_pack():
    pass
