from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True

dark_blue = (0, 0, 139)
blue = (0, 0, 255)
light_green = (144, 238, 144)
green = (0, 255, 0)
red = (255, 0, 0)
nothing = (0, 0, 0,)


def displayColorForTemperature(temperature):
    if -40 < temperature < -10:
        color = dark_blue
    if -9 < temperature < 0:
        color = blue
    if 1 < temperature < 15:
        color = light_green
    if 16 < temperature < 22:
        color = green
    if temperature > 22:
        color = red
    return [color] * 64


def LedsOnForHumidty(percentage):
    number = int((percentage / 100) * 64)
    B = blue
    O = nothing
    logo = [B] * number + (64 - number) * [O]
    return logo


while True:
    option = int(input("Which feature you want to test?0 - exit, 1 - displayColorForTemperature, 2- LedsOnForHumidty"))

    if option == 0:
        break
    if option == 1:
        temperature = int(input("Please input the temperature:"))
        pixels = displayColorForTemperature(temperature)
        s.set_pixels(pixels)
    if option == 2:
        humidty = int(input("Please input the humidty:"))
        pixels = LedsOnForHumidty(humidty)
        s.set_pixels(pixels)
