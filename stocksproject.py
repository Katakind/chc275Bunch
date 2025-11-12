firstdays = open("stocksdays", "r")
buffer1 = firstdays.readlines() [0]
firstdays.close()
print(buffer1)

firstdays = open("stocksdays", "r")
buffer1 = firstdays.readlines() [1]
firstdays.close()
print(buffer1)

firstdays = open("stocksdays", "r")
buffer1 = firstdays.readlines() [2]
firstdays.close()
print(buffer1)

lastdays = open("stocksdays2", "r") 
buffer2 = lastdays.readlines() [0]
lastdays.close()
print(buffer2)

lastdays = open("stocksdays2", "r") 
buffer2 = lastdays.readlines() [1]
lastdays.close()
print(buffer2)

lastdays = open("stocksdays2", "r") 
buffer2 = lastdays.readlines() [2]
lastdays.close()
print(buffer2)

mean = sum/len 