mystring = "hello"
for char in mystring:
    print(char)
    
print("for i loop")
for i in range(len(mystring)):
    print(mystring[i])


print("1. A ")
print("2. B ")
print("3. C ")
print("4. D ")
    
option = input("enter your selection ")
if option.strip().lower() == "A":
    print("            its a A           ")    
elif option.strip().lower() == "B":
    print("           its a B             ")
elif option.strip().lower() == "C":
    print("          its a C         ")
elif option.strip().lower  == "D":
    print("         its a D            ")    
    
option = input("enter a number ")
if option.isnumeric():
    option = int(option)
    ex = option + 5
    print(ex)
else:
    print(f"{option} was not a number")

#isnumeric() returns True if the strings its called on is a number
#/n prints a new line, considered an escape sequence...stands for new line
#.splitlines makes a list out of the lines you want. useful

