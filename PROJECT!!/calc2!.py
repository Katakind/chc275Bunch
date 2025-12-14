check = True
while check == True:
    calc = input("Do you wanna add, subtract, multiply, or divide, or quit ")
    
    if calc == "add":
        try:
            x = int(input("Enter number 1 "))
            y = int(input("Enter number 2 "))
            Piget = x + y
            print(Piget)
        except ValueError:
            print("Both need to be numbers")
    
    elif calc == "subtract":
        try:
            x = int(input("Enter number 1 "))
            y = int(input("Enter number 2 "))
            Mikey = x - y
            print(Mikey)
        except ValueError:
            print("Both need to be numbers")
            
    elif calc == "multiply":    
        try:
            x = int(input("Enter number 1 "))
            y = int(input("Enter number 2 "))
            Sulby = x * y
            print(Sulby)
        except ValueError:
            print("Both need to be numbers")
        
    elif calc == "divide":       
        try:
            x = int(input("Enter number 1 "))
            y = int(input("Enter number 2 "))
            Goober = x/y
            print(Goober)
        except ValueError:
            print("Both need to be numbers")
        except ZeroDivisionError:
            print("donominator must be nonzero")
    
    elif calc == "quit":
     check = False
    