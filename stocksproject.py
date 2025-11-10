firstdays = open("stocksdays", "r")
buffer1 = firstdays.readlines() 
firstdays.close()
print(buffer1)

lastdays = open("stockdays2", "r")
buffer2 = lastdays.readlines()
lastdays.close()
print(buffer2)

