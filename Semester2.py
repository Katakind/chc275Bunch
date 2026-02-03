def foo():
    print("bar")
#1. Def...Tells the python interpreter that you are about to specify a function
#2. Paameter ist... Are your inputs of yyour functions, they go inside the ()

#all the lines after "2" need to be indented 
#when a function ends, you need to unindent the codeblock
foo() #you need to end the function name with parentheses. Pretty much ending with periods in english 


def add(x,y):
    print(x + y)
    
add(6,7) #6 and 7 get plugged in for x and y
# we can add two strings together
add("foo","bar")

def transaction(x):
    tax = x * 0.06
    print(x - tax)
transaction(100)



mylist = [1,2,3,4]
def add10(nums):
    for i in  range(len(nums)):
        nums[i] = nums[i] + 10
        
print(mylist)
add10(mylist)
print(mylist)        


"""
data types in programming can either be mutable or immutable 

- mutable - it can be changed
- immutable - cant be changed

integers are immutable and all numeric types are immutable

BUT lists are mutable
"""

def add7(x):
    x = x + 7
    return x #this is going to flag python to remember that x got reassigned to x + 7

def add(x, y):
    print(x + y) #DONT DO THIS
    
def add(x, y):
    return x + y #do this



#we want a file layout that is (1.) readable (2.) Exposes all of the user implemented functions right as the intereperter starts executing code.
    #exposed = the functon is able to be called
    
#here are the requirements for software engineers:
#1. all of the functions to be exposed to us
#2. dont want code being executed inline with function definitions

"""
How should we lay out our file when we start a project
    -function definitions at the top
    -code to be evaluated at the bottom
    
We can think of functions as services that we can use at the bottom of our file.
"""
#We want to introduce a new structure that is relevant to pretty much all other coding languages. This structure is called the main function!

def foo():
    print("bar")

def fizz(x):
    if x % 2 == 1: #checks if x is even or odd
        print("buzz")
#-----------------------------------------------
def main(): #main is a special kind of function, this only gets evaluated if the parent file is the being exectured
            #he will expand on this later
    check = True
    while check == True:
        print("welcome to the test program")
        print("1. foo")
        print("2. fizz")
        print("type exit to quit")
        option = input("Enter an option: ")
        if option == "1":
            foo()
        if option == "2":
            number = input("wgar is your number? ")
            try:
                number = int(number)
            except Exception as e:
                print(e)
            else:
                fizz(number)
            if option == "quit":
                check = False
                
"""
to call the main function, we need to do a convoluted process in an if statement
"""

if __name__ == "__main__":
    main()