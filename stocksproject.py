firstdays = open("stocksdays", "r")
Microsoft = firstdays.readlines() [0]
firstdays.close()

print("first 20")

Microsoft = Microsoft.split(",")
Microsoft.pop(0)
print(Microsoft)

firstdays = open("stocksdays", "r")
Amazon = firstdays.readlines() [1]
firstdays.close()

Amazon = Amazon.split(",")
Amazon.pop(0)
print(Amazon)

firstdays = open("stocksdays", "r")
Nvidia = firstdays.readlines() [2]
firstdays.close()

Nvidia = Nvidia.split(",")
Nvidia.pop(0)
print(Nvidia)

lastdays = open("stocksdays2", "r") 
Microsoft2 = lastdays.readlines() [0]
lastdays.close()

print("final20")

Microsoft2 = Microsoft2.split(",")
Microsoft2.pop(0)
print(Microsoft2)

lastdays = open("stocksdays2", "r") 
Amazon2 = lastdays.readlines() [1]
lastdays.close()

Amazon2 = Amazon2.split(",")
Amazon2.pop(0)
print(Amazon2)
lastdays = open("stocksdays2", "r") 
Nvidia2 = lastdays.readlines() [2]
lastdays.close()

Nvidia2 = Nvidia2.split(",")
Nvidia2.pop(0)
print(Nvidia2)
