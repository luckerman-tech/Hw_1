while True:
    ship = "Б1В1Г1 Е4Е5 В4В5В6В7 Д3 Д6 З2К2"
    x = input("Введите координату: ")
    if (len(x) != 2) or (x[0].upper() not in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ') or (x[1] not in '123456789'):
        print("Это не координата!")
    else:
        if ship.find(x.upper()) != -1:
            print("Вы попали!")
        else:
            print("Вы не попали!")
        break
    
