init:
    $ mods["start_screen_sb"]= u"Второе дыхание"

    # this var is responsible for playing any sounds
    default persistent.is_sound_play_sb = True
    $ renpy.save_persistent()

    # this var - show popup with achivment or not
    $ is_achiv_show_sb = True

    # and this - include adult scenes in scenario or not
    $ is_adult_mode_sb = False