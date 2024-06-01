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