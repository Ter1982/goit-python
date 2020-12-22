

while True:
    
        x = float(input("Enter number:"))
   
        user_input = input("Enter operator (+,-,*,/): ")

        y = float(input("Enter number:"))

        z = input("Enter operator( = ):")
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
                print("Деление на ноль!")
        else:
            print("Не верный ввод") 
                   
               
        
    