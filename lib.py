import math

colors = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "gray": (122, 122, 122),
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255)
}

def deg_to_rad(degrees):
    return degrees * math.pi / 180