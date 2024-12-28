def avg(a,b,c):
    return (a+b+c)/3

a=[]
for i in range(3):
   marks=int(input("Enter marks of the subjects :"))
   a.append(marks)
avgMarks=avg(a[0],a[1],a[2])
print("Average Marks is : ",avgMarks)