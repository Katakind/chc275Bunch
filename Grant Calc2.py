check = True
while check == True:
    calc = input("Do you wanna: Add, Subtract, Multiply, Divide, or quit")

    if calc == "Add":
        try:
            x = int(input("Enter number 1 "))
            y = int(input("Enter number 2 "))
            Solution = x + y
            print(Solution)
        except ValueError:
            print("Both need to be numbers")
            
    elif calc == "Subtract":
        try:
            x = int(input("Enter number 1 "))
            y = int(input("Enter number 2 "))
            Solution2 = x - y
            print(Solution2)
        except ValueError:
                print("Both need to be numbers")
                
    elif calc == "Multiply":
        try:
            x = int(input("Enter number 1 "))
            y = int(input("Enter number 2 "))
            Solution3 = x * y
            print(Solution3)
        except ValueError:
            print("Both need to be numbers")
            
    elif calc == "Divide":
        try:
            x = int(input("Enter number 1 "))
            y = int(input("Enter number 2 "))
            Solution4 = x / y
            print(Solution4)
        except ValueError:
            print("Both need to be numbers")
        except ZeroDivisionError:
            print("denominator cant be zero")
    
    elif calc == "quit":
        check = False