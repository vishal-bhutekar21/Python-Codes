with open("demo1.txt", "r") as f: 
    line=0
    data=1
    while data:
        data=f.readline()
        if("Vishal" in data):
            print("vishal found at line on :",line)
        line +=1
    
 