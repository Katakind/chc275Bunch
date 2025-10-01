mylist = [10,20,30,40,50]

print("example 1")
for i in range(len(mylist)):
    print(mylist[i])
    
print("example 2")    
for num in mylist:
    print(num)

print("example 3")  
i = 0
while i < len(mylist):
    print(mylist[i])
    i = i + 1
    
print("example 4")
names = ["may", "zato", "dizzy"]
print(names)

names.append("dizzy") #adds set variable to the list.
print(names)

names.remove("zato")
print(names)

names.pop(0) #does same thing as remove, but instead puts it in a hidden storage.
print(names)

"""
print("example idek")
names = []
check = False
while check == False:
    names = input("Enter the name you want to add to the list or quit: ")
    if names == "quit":
        check = True
    else:
        names.append(names) 
print(names) 

"""

students = ["caspar, sylvain, ferdinand"]
GPAs = [32, 87, 93]

for i in range(len(students)):
    print(f"(students: {students} (GPA: {GPAs})") #cant get to run
    
    