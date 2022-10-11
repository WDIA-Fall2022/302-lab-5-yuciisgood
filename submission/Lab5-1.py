import random
from sense_hat import SenseHat

s = SenseHat()
s.low_light = True
green = (0, 255, 0)
nothing = (0, 0, 0,)


def rollAdice(number_of_faces):
    return random.randint(1, number_of_faces)

if __name__ == '__main__':
    while True:
        try:
            number = int(input("Please input the number of faces"))
            if number >= 65:
                raise Exception("Sorry,the number can not over 65")
        except:
            print("This is not a legal input")
        else:
            break
    result = rollAdice(number)
    G = green
    O = nothing
    logo = [G] * result + (64 - result) * [O]
    s.set_pixels(logo)
