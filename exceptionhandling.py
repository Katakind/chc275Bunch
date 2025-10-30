try:
    x = [1,2,3]
    y = int(input("Enter Number 1 "))
    Number2 = x/y
    print(Number2)
except ValueError:
    print("Both need to be numbers")
except ZeroDivisionError:
    print("donominator must be nonzero")
except Exception as e:
    print(e)        
    
try:
    x = int(input("Enter Number 1 "))
    y = int(input("Enter Number 2 "))
    Number2 = x/y
    print(Number2)
except ValueError:
    print("Both need to be numbers")
except ZeroDivisionError:
    print("donominator must be nonzero")
except Exception as e:
    print(e)        