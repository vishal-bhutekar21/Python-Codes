f2=open("demo.txt","w")
f1=open("demo1.txt","r")

f2.write(f1.read())
f1.close()
f2.close()
print("The data written in the file ")