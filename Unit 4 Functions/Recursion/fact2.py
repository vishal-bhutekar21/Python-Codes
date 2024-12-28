no=int(input("Enter any number to find its factorail :"))
def fact(n):
    if n==0 or n==1:
        return 1
    else:
       return n* fact(n-1)

facttt=fact(no)
print(f"factorial of {no} is",facttt)