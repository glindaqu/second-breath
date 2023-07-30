screen main_menu_sb:
    tag menu 
    modal True

    imagemap:
        ground u"mods/secondBreath/source/bg/bg_main.png"
        idle u"mods/secondBreath/source/ui/nav_blr.png"
        hover u"mods/secondBreath/source/ui/nav_hov.png"

        #start
        hotspot(815, 451, 237, 78) action Jump("prolog_sb")

        #settings
        hotspot(815, 566, 327, 78) action Jump("settings_screen_sb")

        #exit
        hotspot(815, 681, 262, 78) action Jump("exit_sb")
        


label start_screen_sb:
    if persistent.is_sound_play_sb:
        play music celestial_sb if_changed
    call screen main_menu_sb


label exit_sb:
    return
        