while (true) {
    console.log(input.lightLevel())
    light.setBrightness(3)
    if (input.lightLevel() < 6) {
        light.setAll(color.rgb(255, 0, 0))
    } else {
        light.setAll(color.rgb(0, 255, 0))
    }
    
}
