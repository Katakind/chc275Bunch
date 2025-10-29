mystring = "Kazuma Subaru Rudy"
names = mystring.split()
print(names)

mystring = "1010101010hello1010101010"
msg = mystring.split("1010101010")
print(msg)

space = " "
newmsg = space.join(msg)
print(newmsg)

newmsg = space.join(msg).strip()
print(newmsg)

newmsg = " ".join(msg)
print(newmsg)
0
#know .lower() .uppper() .strip() .isnumeric() .split() .splitlines() .join()

string = "Buenos "
string2 = "Dias "
joined = string + string2
print(joined)
#DONT
joined = string2 + string 
print(joined)