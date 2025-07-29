import random
try:
    i=0
    while i<100:
        num=random.randint(1,101)
        print("Number: {} ".format(num),end='-')
        
        if num%2==0:
            print("Even Number")
        else:
            print("Odd Number")
        i+=1
        
except Exception as e:
    print(e)
    print("Please Check The Code")