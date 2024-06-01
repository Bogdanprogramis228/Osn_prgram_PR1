print("\n8 ЗАВДАННЯ\n") 

m = int(input("Введіть значення m (порядковий номер студента у журналі): "))

if m > 25:
    print("m не може бути більше 25")
else:
    combinations = 1
    for i in range(25, 25 - m, -1):
        combinations *= i

print(f"Кількість можливих комбінацій: {combinations}")