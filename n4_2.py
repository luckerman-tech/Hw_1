while True:
    k = 0
    name = input("Введите ваше имя: ")
    for i in range(0, len(name)):
        if name[i].upper() in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ':
            k += 1
    if name[0].upper() in 'ЙЪЫЬ':
        k -= 1
    if k == len(name):
        break
    else:
        print("Недопустимое имя!")
while True:
    k = 0
    surname = input("Введите вашу фамилию: ")
    for i in range(0, len(surname)):
        if surname[i].upper() in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ':
            k += 1
    if surname[0].upper() in 'ЙЪЫЬ':
        k -= 1
    if k == len(surname):
        break
    else:
        print("Недопустимая фамилия!")
while True:
    k = 0
    age = input("Введите ваш возраст: ")
    for i in range(0, len(age)):
        if age[i] in '0123456789':
            k += 1
    if (age[0] == "0") or (int(age) > 130):
        k -= 1
    if k == len(age):
        break
    else:
        print("Недопустимый возраст!")
print("Ваше имя: {0}, фамилия: {1}, возраст: {2} лет.".format(name, surname, age))
print(f"Ваше имя: {name}, фамилия: {surname}, возраст: {age} лет.")



