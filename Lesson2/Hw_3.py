while True:

    try:
        x = float(input('Введите первое число:'))
    except ValueError:
        print('неправильный ввод числа')
        continue
    while True:

        user_input = input('Введите оператор (+,-,*,/): ')
        if user_input not in ('+', '-', '*', '/'):
            print('неверный оператор выражения')
            continue
        while True:

            try:
                y = float(input('Введите второе число:'))
            except ValueError:
                print('неправильный ввод числа')
                continue
            while True:
                z = input('Введите оператор( = ):')
                if z != '=':
                    print('неверный оператор ввода ровно')
                    continue

                if user_input == '+':
                    print(x + y)
                elif user_input == '-':
                    print(x - y)
                elif user_input == '*':
                    print(x * y)
                elif user_input == '/':
                    if y != 0:
                        print(x / y)
                    else:
                        print('Деление на ноль')

                break
            break
        break
    break
