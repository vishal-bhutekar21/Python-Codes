movies=[]
# names=input("Enter any three movies names :").split()
# print(names)
# movies.append(names)
# print(movies)

for i in range(3):
    movies.append(input(f"Eneter {i+1} movie names :"))

for i in range(len(movies)):
    print(f"The {i+1} movies is :",movies[i])
    
    
for i in range(len(movies)):
    print("The {} movies is :".format(i+1),movies[i])
     