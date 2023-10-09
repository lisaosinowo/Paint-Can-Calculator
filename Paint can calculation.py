import math
def paint_calc(height, width, coverage):
    number_of_cans = (height * width)/coverage
    number_of_full_cans = round(number_of_cans, 1)

    print(f"You'll need {math.ceil(number_of_full_cans)} cans of paint.") # math.ceil rounds any decimal number to the next whole number. e.g 3.2 = 4, 5.4 = 6, 7.3 = 8, 6.8 = 7


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

paint_calc(height = test_h, width = test_w, coverage = 5)
