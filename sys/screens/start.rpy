screen main_menu_sb:
    tag menu 
    modal True
    add u"mods/secondBreath/source/bg/bg.png"

    #title
    imagebutton:
        idle u"mods/secondBreath/source/ui/Label.png"
        hover u"mods/secondBreath/source/ui/Label.png"
        xpos 833
        ypos 134
        action NullAction()

    #frame
    imagebutton:
        idle u"mods/secondBreath/source/ui/frame.png"
        hover u"mods/secondBreath/source/ui/frame.png"
        xpos 468
        ypos 258
        action NullAction()

    #start
    imagebutton:
        idle u"mods/secondBreath/source/ui/start.png"
        hover u"mods/secondBreath/source/ui/start.png"
        xpos 809
        ypos 472
        action NullAction()

    #settings
    imagebutton:
        idle u"mods/secondBreath/source/ui/sett.png"
        hover u"mods/secondBreath/source/ui/sett.png"
        xpos 809
        ypos 587
        action NullAction()

    #exit
    imagebutton:
        idle u"mods/secondBreath/source/ui/ex.png"
        hover u"mods/secondBreath/source/ui/ex.png"
        xpos 809
        ypos 702
        action NullAction()


label start_screen_sb:
    call screen main_menu_sb
        