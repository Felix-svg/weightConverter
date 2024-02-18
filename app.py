import math

weight = float(input("Enter your weight: "))
unit = input("(K)g or (L)bs: ")

if unit.upper() == "K":
    converted_unit = math.floor(weight / 0.45)
    print("Weight in lbs: " + str(converted_unit))
elif unit.upper() == "L":
    converted_unit = math.floor(weight * 0.45)
    print("Weight in kgs: " + str(converted_unit))
else:
    print("Please enter a valid unit")