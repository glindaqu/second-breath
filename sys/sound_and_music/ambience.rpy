init -444:
    $ absolute_way = u"mods/secondBreath/source/ambience/"

    $ bus_int_sb = absolute_way + "bus_int.mp3"
    $ bus_quiet_sb = absolute_way + "bus_quiet.mp3"
    $ bus_stop_sb = absolute_way + "bus_stop.mp3"

init python:
    renpy.music.register_channel("ambient", "sfx", loop=True, tight=True)