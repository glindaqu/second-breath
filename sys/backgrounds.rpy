init:
    $ absolute_way = u"mods/secondBreath/source/bg/" 

    image bg coffee house sb = absolute_way + u"coffee_market.png"
    image bg classroom sb = absolute_way + u"classroom_night.png"
    image bg bus window sb = absolute_way + u"bus_window.png"
    image bg none sb = absolute_way + u"none.png"
    image bg room sb = absolute_way + u"room.png"
    image bg kitchen sb = absolute_way + u"kitchen.png"
    image bg outdoor sb = absolute_way + u"out.png"

    image bg bus stop sb = ConditionSwitch(
        "persistent.sprite_time=='day'", absolute_way + u"bus_stop_day.png",
        "persistent.sprite_time=='night'", absolute_way + u"bus_stop_night.png"
    )

    image bg city street sb = ConditionSwitch(
        "persistent.sprite_time=='day'", absolute_way + u"city_street_day.png",
        "persistent.sprite_time=='night'", absolute_way + u"city_street_night.png"
    )