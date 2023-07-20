screen settings_menu_sb:
    tag menu 
    modal True

    add u"mods/secondBreath/source/bg/bg_settings.png"

    #navigation
    imagebutton:
        xpos 694
        ypos 390
        idle u"mods/secondBreath/source/ui/settings_nav.png"
        hover u"mods/secondBreath/source/ui/settings_nav.png"
        action NullAction()
        
    #exit
    imagebutton:
        xpos 46
        ypos 36
        idle u"mods/secondBreath/source/ui/exit_ico_blr.png"
        hover u"mods/secondBreath/source/ui/exit_ico_hov.png"
        action Jump("start_screen_sb")
    
    #sound toggle
    imagebutton:
        xpos 1100
        ypos 398

        if is_sound_play_sb:
            idle u"mods/secondBreath/source/ui/checked.png"
            hover u"mods/secondBreath/source/ui/checked.png"
        else:
            idle u"mods/secondBreath/source/ui/unchecked.png"
            hover u"mods/secondBreath/source/ui/unchecked.png"
        action SetVariable("is_sound_play_sb", not is_sound_play_sb), PauseAudio("music", is_sound_play_sb)

    #achiv toggle
    imagebutton:
        xpos 1100
        ypos 476
        if is_achiv_show_sb:
            idle u"mods/secondBreath/source/ui/checked.png"
            hover u"mods/secondBreath/source/ui/checked.png"
        else:
            idle u"mods/secondBreath/source/ui/unchecked.png"
            hover u"mods/secondBreath/source/ui/unchecked.png"
        action SetVariable("is_achiv_show_sb", not is_achiv_show_sb)

    #adult toggle
    imagebutton:
        xpos 1100
        ypos 554
        if is_adult_mode_sb:
            idle u"mods/secondBreath/source/ui/checked.png"
            hover u"mods/secondBreath/source/ui/checked.png"
        else:
            idle u"mods/secondBreath/source/ui/unchecked.png"
            hover u"mods/secondBreath/source/ui/unchecked.png"
        action SetVariable("is_adult_mode_sb", not is_adult_mode_sb)


label settings_screen_sb:
    call screen settings_menu_sb
        