name = []
grade = []
file = open("randofile.txt", "w")

buffer = []


for i in range(len(name)):
    line = f"{"name[i]"}, {"grade{i}"}/n"
    buffer.apend(line)
    
buffer[-1] = buffer[-1].strip

file.writelines(buffer)
file.close()  

name.append("william")
grade.append("32")
file.write(line)
file.close()
