init -1:
    image uvao winter normal sb = ConditionSwitch(
        "persistent.sprite_time=='night'", im.MatrixColor("mods/secondBreath/source/sprite/uvao/normal.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, "mods/secondBreath/source/sprite/uvao/normal.png"
    )