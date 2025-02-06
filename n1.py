while True:
    x = input("Введите целое неотрицательное число (для выхода из программы введите 'exit'): ")
    if x.isdigit():
        print("Длина числа:", len(x))
    elif x == "exit":
        break
    else:
        print("Это не целое неотрицательное число!")
