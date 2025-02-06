while True:
    x = input("Введите целое неотрицательное число (введите 'exit' для выхода из программы): ")
    if x.isdigit():
        print("Все числа в интервале [-x; x+1]:")
        minus = 0
        plus = 0
        for a in range(-int(x), int(x)+2):
            print(a)
            if a < 0:
                minus += a
            else:
                plus += a
        print("Сумма отрицательных чисел из интервала:", minus)
        print("Сумма положительных чисел из интервала:", plus)
    elif x == "exit":
        break
    else:
        print("Это не целое неотрицательное число!")
    
