import math
import random
from colorama import Fore
from colorama import Style

print(f"{Fore.RED}**********************************************{Style.RESET_ALL}")
print(f"{Fore.GREEN}*           Paint Area Calculator            *{Style.RESET_ALL}")
print(f"{Fore.YELLOW}**********************************************\n{Style.RESET_ALL}")

# def get_painting_area():
#     wall_height = random.randint(1, 101)
#     wall_width = random.randint(1, 101)
#     area = wall_width * wall_height
#     return area
COVERAGE = 5


def get_painting_area(wall_height, wall_width):
    area = wall_width * wall_height
    return area


def amount_of_paint_cans_needed(area):
    # 1 can of paint = 5 sqm coverage
    cans_needed = math.ceil(area / COVERAGE)
    return cans_needed


def input_wall_dimensions():
    wall_height, wall_width = map(float, input("please enter the height and width of the wall:").split())
    return wall_height, wall_width


wall_height, wall_width = input_wall_dimensions()

area = get_painting_area(wall_height, wall_width)

cans_needed = amount_of_paint_cans_needed(area)

print(f"Area to be painted is: {area} sqm which will require {cans_needed} cans of paint")
