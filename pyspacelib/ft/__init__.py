from pyspacelib.ft.ft import deviceMap, ftclient

flaschen_taschen = ftclient(deviceMap["Flaschen Taschen"],
                            layer=11,
                            transparent=False)
noise_table = ftclient(deviceMap["Noise Square Table"],
                       layer=15,
                       transparent=True)
