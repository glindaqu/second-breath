init -666:

    #   Юля, зима --------------------------------------------------------------------------

    image uvao winter normal sb = ConditionSwitch(
        "persistent.sprite_time=='night'", im.MatrixColor("mods/secondBreath/source/sprite/uvao/normal.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, "mods/secondBreath/source/sprite/uvao/normal.png"
    )

    image uvao winter confuse sb = ConditionSwitch(
        "persistent.sprite_time=='night'", im.MatrixColor("mods/secondBreath/source/sprite/uvao/confuse.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, "mods/secondBreath/source/sprite/uvao/confuse.png"
    )

    image uvao winter surprise sb = ConditionSwitch(
        "persistent.sprite_time=='night'", im.MatrixColor("mods/secondBreath/source/sprite/uvao/surprise.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, "mods/secondBreath/source/sprite/uvao/surprise.png"
    )

    image uvao winter smile sb = ConditionSwitch(
        "persistent.sprite_time=='night'", im.MatrixColor("mods/secondBreath/source/sprite/uvao/smile.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, "mods/secondBreath/source/sprite/uvao/smile.png"
    )

    image uvao winter laugh sb = ConditionSwitch(
        "persistent.sprite_time=='night'", im.MatrixColor("mods/secondBreath/source/sprite/uvao/laugh.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, "mods/secondBreath/source/sprite/uvao/laugh.png"
    )
    # ---------------------------------------------------------------------------------------------