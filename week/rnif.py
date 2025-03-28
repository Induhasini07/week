import random
n=random.randint(1,100)
while(True):
    x=int(input("enter the number"))
    if (x<n):
        print("to low")
    elif (x>n):
        print("to high")
    else :
        print( "got the number")
        break;
