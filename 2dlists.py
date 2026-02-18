grid = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
"""
each list inside a list is called a row
we can access individual rows by typing:
grid[row][col] 
"""
box = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(box[2][0]) #prints 7

print(box[1])

#lets talk about iterating over a 2d list
# 1) for each loop = easiest to use, least amount of flexibility 
# 2) for i-loop = moderate difficulty to use, good amount of flexibility
# 3) while loop = hardest difficulty to use, most amount of flexibility in terms of stopping conditions, breaks, etc



#for each loop. we need 2. an outer and an inner

sol = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for row in sol:
    for num in row:
        print(num) #prints 1-9
        
        
#for-i loops require a few things. 
# 1) a range of values
# 2) i need a length to pass into range()

sol2 = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

for i in range(len(sol2)):
    for j in range(len(sol2[0])):
        print(f"({i},{j}) = {sol2[i][j]}", end = "")
        
