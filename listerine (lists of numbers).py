Kiske = [1,2,3,4,5]
print(Kiske)
print(Kiske[0])
print(Kiske[0] * Kiske[3]) 
print(Kiske[-1]) 

#directly ACCESSING the list
i = 0
while i <= 3:
    print(Kiske[i])
    i = i + 1

#doing the same thing as a "while" loop but in a different way   
sol = [5,10,15,20]
print("with forloop")
for num in sol:
    print(num)

#creating copies of elements of the list
i = 0
while i <= 3:
    sol[i] = sol[i] + 5
    i = i + 1
print(sol)    

