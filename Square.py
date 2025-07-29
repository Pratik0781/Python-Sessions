try:
    num=eval(input("Please enter the number :"))
    square=num*num
    print("Square of {} is :{}".format(num,square))
except Exception as e:
    print(e) # When Error Is Come then Except block is run
    print("Check the code there is error")