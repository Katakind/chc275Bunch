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


for i in range(len(Microsoft)):
    Microsoft[i] = int(Microsoft[i])
    Amazon[i] = int(Amazon[i])
    Nvidia[i] = int(Nvidia[i])
    Microsoft2[i] = int(Microsoft2[i])
    Amazon2[i] = int(Amazon2[i])
    Nvidia2[i] = int(Nvidia2[i])
N1 = sum(Nvidia)/ len(Nvidia)
M1 = sum(Microsoft)/ len(Microsoft)
A1 = sum(Amazon)/ len(Amazon)
N2 = sum(Nvidia2)/ len(Nvidia2)
M2 = sum(Microsoft2)/ len(Microsoft2)
A2 = sum(Amazon2)/ len(Amazon2)
print(M1)
print(A1)
print(N1)
print(M2)
print(A2)
print(N2)

Buys = []

    
if M2 > M1:
    Buys.append("Microsoft" )
if A2 > A1:
    Buys.append("Amazon")
if N2 > N1:
    Buys.append("Nvidia")
    
buffer = []
line0 = f"Microsoft average1 {M1} average2 {M2}\n"
line1 = f"Amazon average1 {A1} average2 {A2}\n"
line2 = f"Nvidia average1 {N1} average2 {N2}\n"
line3 = f"Buys: {Buys}"
Buffer= [line0,line1,line2,line3]

file = open("report.txt.","w")
file.writelines(Buffer)
file.close 