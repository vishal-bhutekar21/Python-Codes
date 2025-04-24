class WorkerException(Exception):
     pass
    


try:
    arr=[1,2,3,4,5]
    # age=int(input("Enter the age of the worker :"))
    # if age<18 and age>50:
    #     raise WorkerException
    
    print("The result is :",(arr[100]))
    
except Exception as e:
    print("this is index out of range exception",e)
    
# except WorkerException:
#     print("Worker age is valid for the job")
# else:
#     print("Worker age is not valid for the job")
    




