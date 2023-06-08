#this is my tossing coin
import random
for i in range(0,5):
    r=random.randint(0,2) 
    a=int (input("h =1 or t =2: "))
    if a==r:
        print("you win")
    else:
        print("you lost")