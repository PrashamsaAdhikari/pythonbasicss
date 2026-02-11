f= open("myfile.txt", "r")
text=f.read()
f.close()
print(text)

f= open("myfile2.txt", "w")
text=f.write("i'm writing ")
f.close()
print(text)

file = open("myfile2.txt", "a")
file.write("New line")
