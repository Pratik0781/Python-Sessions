import random
try:
    sum=0
    i=1
    while i<11:
    
        num=random.randint(1,100)
        print(i,"number=",num)
        sum=sum+num
        print("Sum Of {} Random Numbers Is:{}".format(i,sum))
        i=i-1
    
except Exception as e:
    print(e)