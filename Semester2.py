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

