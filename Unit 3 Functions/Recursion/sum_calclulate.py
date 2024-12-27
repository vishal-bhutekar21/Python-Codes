def sum(n):
     if n==0:
         return 0
     return n+sum(n-1)
 
no = int(input("Enter any no to find its sum :"))
print(sum(no))