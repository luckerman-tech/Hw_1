while True:
    x = input("Введите целое неотрицательное трёхзначное число с различными цифрами (введите 'exit' для выхода из программы): ")
    if x.isdigit() and len(x) != 3:
        print("Число не трёхзначное!")
    elif x.isdigit():
        a = int(x) // 100
        b = (int(x) - a*100) // 10
        c = (int(x) - a*100 - b*10)
        if a == b or a == c or b == c:
            print("В числе есть повторяющиеся цифры!")
        else:
            print("Числа, образованные при перестановке цифр заданного числа:")
            print(a*100 + b*10 + c)
            print(a*100 + c*10 + b)
            print(b*100 + a*10 + c)
            print(b*100 + c*10 + a)
            print(c*100 + a*10 + b)
            print(c*100 + b*10 + a)
    elif x == "exit":
        break
    else:
        print("Это не целое неотрицательное число!")
