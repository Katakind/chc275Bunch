exitcondition = False 
foodlist = []
carts = []
quanity = []
cartprice = []
while exitcondition == False:
    print("Welcome to the grocery store of doom and despair")
    print("1. add to cart")
    print("2. remove from cart")
    print("3. check out")
    storesystem = input("select an option ")
    
    if storesystem == "add to cart":
        print(foodlist)
        foodselection = input("Choose which you want")
    
    
    elif storesystem == "remove from cart":
        print(carts) 
        input("select which to remove")
       