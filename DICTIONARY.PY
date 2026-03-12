"""
Dictionaries == Hashmaps/Hash tables in other programming langauges
schema = defining structure of the data
a dictionary is an UNORDERED list where the elements are (key, value) pairs
"""

mydict = {}
        #curley braces to define a dictionary
        
mydict2 = {"johnkaisen":1000, "KyleJujustu":0, "Joseph":250 }
#how do we retrieve from a dictionary? square brackets of course
print(mydict2["johnkaisen"])

"""
Lets talk about keys:
    -what is allowed to be a key?
        -Mutables: Lists
        -Immutables: strings, numerics
        -Immutables are the only things allowed to be keys. because of the hash function.
        Vertical Line Test: Every X value has Exactly ONE Y value
        Keys can ONLY have one value because of that
        
Let's talk about Values: What can be a value??? ANYTHING
Lists, YES
Strings, YES
Ints, Yes
another dictionary? YES
"""
mydict3 = {1: ["a", "b", "c"], 2:{"foo":10}, 3:True}
print(mydict3)

print(mydict3[1][0]) #should print A
print(mydict3[2]["foo"])
"""
How to remove things. 2 ways. 
The unsafe way 1) del keyword <- this just zaps the key/value pair from memory
"""
del mydict2["johnkaisen"]
print(mydict2)

"""
The safer way 2) .pop()
for a list this takes in ONE value
but for a dictionary, it takes in two parameters. either get rid of it, or trigger a "keyerror"
"""

mydict2.pop("Joseph","usernotfound")
print(mydict2)

