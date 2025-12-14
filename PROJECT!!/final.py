x = input("put any number you want and watch it turn to 1! ")
x = int(x)
check = True
while check == True:
    print(x)
    if x == 1:
        check = False 
    if x % 2 == 0:
        x= x / 2
    elif x % 2 == 1:
        x = x * 3 + 1