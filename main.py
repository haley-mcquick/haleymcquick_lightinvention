while True:
    print(input.light_level())
    light.set_brightness(3)
    if input.light_level() < 6:
        light.set_all(color.rgb(255, 0, 0))
    elif input.light_level() > 15:
        light.set_all(color.rgb(255, 255, 0))
    else:
        light.set_all(color.rgb(0, 255, 0))