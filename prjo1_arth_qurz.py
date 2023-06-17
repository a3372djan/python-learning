import random
class Arthmetic:
    def add(a,b):
        result=a+b
        return result

    def subtract(a,b):
        result=a-b
        return result


    def multiply(x,y):
        result=x*y
        return result

    def divide(w,v):
        result=w/v
        return result


    def reminder(w,v):
        result=w%v
        return result


    def percentase(m,t):
        result=m*100/t
        return result
    def hello(n):
        print(f"hello and wellcome {n}")
    def check(q,a):
        if q==a:
            print("Correct!")
            return 10
        else:
            print("Wrong! ")
            return 0

        
total_points=0
 
arth=Arthmetic
name=input("what is your name ")
max_question=int(input("question#"))
arth.hello(name)
for i in range(0,max_question):
    r1=random.randint(1,10)
    r2=random.randint(1,10)
    op=random.randint(1,3)
    if op==1:
        result=arth.add(r1,r2)
        q=int(input(f"{r1} + {r2} = ?"))
        points=arth.check(q,result)

    elif op==2:
        result=arth.subtract(r1,r2)
        q=int(input(f"{r1} - {r2} = ?"))
        points=arth.check(q,result)
    elif op==3:
        result=arth.multiply(r1,r2)
        q=int(input(f"{r1} x {r2} = ?"))
        points=arth.check(q,result)
    elif op==4:
        result=arth.reminder(r1,r2)
        q=int(input(f"{r1} % {r2} = ?"))
        points=arth.check(q,result)
    print (f"you gat {points}")
    total_points=total_points+points
print(f"----- your total points={total_points}--------")







