with open("demo1.txt", "r") as f:
    data = f.read()  
    
    if(data.find("Vishal") !=-1):
        print("word found in the file ")
    else:
        print("data not available in the file ")
    
 