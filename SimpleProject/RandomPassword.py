import random as a
import string as s

print("All the lowercase values are :",s.ascii_lowercase)
print("All the uppercase values are :",s.ascii_uppercase)
print("All asciii letters are :",s.ascii_letters)
print("All digits are :",s.digits)
print("All punctuation area ",s.punctuation)


values=s.ascii_letters+s.digits+s.punctuation

passwords=[]
passlen=12

for i in range (passlen):
    passwords.append(a.choice(values))


print("your password is : ","".join(passwords))