with open("demo1.txt", "r") as f:
    data = f.read()  
    
    if(data.count("Vishal") ):
        print("word found in the file ",data.count("Vishal"))
        data.capitalize()
    else:
        print("data not available in the file ")
    
 