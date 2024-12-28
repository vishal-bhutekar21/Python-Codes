f1=open("demo1.txt","r")

print(f1.read(55))
print("The type of the variable is :",f1)

f2=open("demo1.txt","r")

firstline=f2.readline()

print("The file f2 pointer ends here ")
print(firstline,"this is the first Line in the file")
f1.close()
f2.close()