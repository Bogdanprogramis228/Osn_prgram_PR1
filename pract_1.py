import math

print("\n1 ЗАВДАННЯ\n") 

print("Twinkle, twinkle, little star, \n \t How I wonder what you are! \n \t \t Up above the world so high, \n \t \t Like a diamond in the sky. \n Twinkle, twinkle, little star, \n \t How I wonder what you are")

print("\n2 ЗАВДАННЯ\n") 

def find_area(radius):
    return math.pi * radius * radius

radius = float(input("Введіть радіус кола: "))
area = find_area(radius)
print(f"Площа кола з радіусом {radius} дорівнює {area}")

print("\n3 ЗАВДАННЯ\n") 

color_list = ["Red", "Green", "White", "Black"]

first_color = color_list[0]
last_color = color_list[-1]

print(f"Перший колір: {first_color}")
print(f"Останній колір: {last_color}")

print("\n4 ЗАВДАННЯ\n") 

n = int(input("Введіть ціле число: "))
n_str = str(n)
nn = int(n_str * 2)
nnn = int(n_str * 3)
result = n + nn + nnn

print(f"Результат обчислення {n} + {nn} + {nnn} дорівнює {result}")

print("\n5 ЗАВДАННЯ\n") 

numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 
    953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 
    626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 
    379, 843, 831, 445, 742, 717, 958, 743, 527
]

for number in numbers:
    if number == 237:
        break
    if number % 2 == 0:
        print(number)

print("\n6 ЗАВДАННЯ\n") 

number_list = ["01010101", "00011100011"]

for number in number_list:
    valid = True
    i = 0
    n = len(number)
    
    while i < n:
        if number[i] == '0':
            
            zero_count = 0
            while i < n and number[i] == '0':
                zero_count += 1
                i += 1
            
            one_count = 0
            while i < n and number[i] == '1':
                one_count += 1
                i += 1
            
            if zero_count != one_count:
                valid = False
                break
        else:
            i += 1
            
    print(valid)
    
print("\n7 ЗАВДАННЯ\n") 

n = int(input("Введіть значення n: "))
m = int(input("Введіть значення m (порядковий номер студента у журналі): "))

for i in range(-n, n+1, m):
    if i % 2 == 0:
        print(i)

print("\n8 ЗАВДАННЯ\n") 

m = int(input("Введіть значення m (порядковий номер студента у журналі): "))

if m > 25:
    print("m не може бути більше 25")
else:
    combinations = 1
    for i in range(25, 25 - m, -1):
        combinations *= i

print(f"Кількість можливих комбінацій: {combinations}")

print("\n9 ЗАВДАННЯ\n") 

my_list = [1, 2, 3, 4, 5]

L = [3, 6, 7]
my_list.extend(L)
print("Після додавання L:", my_list)

my_list.insert(1, 33333)
print("Після вставлення 33333:", my_list)

my_list.reverse()
print("У зворотньому порядку:", my_list)

my_list.append(3)
print("Після додавання 3:", my_list)

my_list.remove(3)
print("Після видалення першого 3:", my_list)

my_list.sort()
print("У порядку збільшення:", my_list)

my_list.clear()
print("Після очищення списку:", my_list)

print("\n10 ЗАВДАННЯ\n") 

user = {
    "ID": 1,
    "Прізвище": "Бойчук",
    "Ім’я": "Богдан",
    "Група": "ІПЗс-21-1",
    "Курс": 3,
    "Книги (борг)": [],
    "Статистика книг": []
}

def print_reader_card(user):
    print("Карта читача:")
    print(f"ID: {user['ID']}")
    print(f"Прізвище: {user['Прізвище']}")
    print(f"Ім’я: {user['Ім’я']}")
    print(f"Група: {user['Група']}")
    print(f"Курс: {user['Курс']}")
    print(f"Книги (борг): {', '.join(user['Книги (борг)']) if user['Книги (борг)'] else 'Немає'}")
    print(f"Статистика книг: {', '.join(user['Статистика книг']) if user['Статистика книг'] else 'Немає'}")

print_reader_card(user)

while True:
    print("\nМеню:")
    print("1 - Показати карту читача")
    print("2 - Взяти книгу")
    print("3 - Повернути книгу")
    print("0 - Вийти")
    
    choice = input("Введіть ваш вибір: ")
    
    if choice == "0":
        break
    elif choice == "1":
        print_reader_card(user)
    elif choice == "2":
        book_name = input("Введіть назву книги, яку хочете взяти: ")
        user["Книги (борг)"].append(book_name)
        print(f"Книга '{book_name}' додана до боргу.")
    elif choice == "3":
        if not user["Книги (борг)"]:
            print("У вас немає книг у боргу.")
        else:
            print(f"Книги у боргу: {', '.join(user['Книги (борг)'])}")
            book_name = input("Введіть назву книги, яку хочете повернути: ")
            if book_name in user["Книги (борг)"]:
                user["Книги (борг)"].remove(book_name)
                user["Статистика книг"].append(book_name)
                print(f"Книга '{book_name}' повернута.")
            else:
                print(f"Книга '{book_name}' відсутня у вашому боргу.")
    else:
        print("Невірний вибір. Спробуйте ще раз.")
       
print("\n Частина 2 \n")
print("\n Завдання 1 \n") 