screen main_menu_sb:
    tag menu 
    modal True

    imagemap:
        ground u"mods/secondBreath/source/bg/bg_main.png"
        idle u"mods/secondBreath/source/ui/nav_blr.png"
        hover u"mods/secondBreath/source/ui/nav_hov.png"

        #start
        hotspot(815, 451, 237, 100) action Jump("prolog_sb")

        #settings
        hotspot(815, 566, 327, 100) action Jump("settings_screen_sb")

        #exit
        hotspot(815, 681, 262, 100) action NullAction()
        


label start_screen_sb:
    if is_sound_play_sb:
        play music u"mods/secondBreath/source/music/Celestial.mp3" if_changed
    call screen main_menu_sb



        