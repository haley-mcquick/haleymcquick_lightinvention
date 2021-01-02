while True:
    print(input.light_level())

if input.light_level() < 6:
    light.set_all(color.rgb(255, 0, 0))
else:
    light.set_all(color.rgb(0, 255, 0))
