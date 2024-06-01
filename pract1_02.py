import math
print("\n2 ЗАВДАННЯ\n") 

def find_area(radius):
    return math.pi * radius * radius

radius = float(input("Введіть радіус кола: "))
area = find_area(radius)
print(f"Площа кола з радіусом {radius} дорівнює {area}")