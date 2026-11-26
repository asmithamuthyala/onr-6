'''
name="codegnan"     #global
def Local():
    x=10     #local variable
    print(x)
    name="techgnan"
    print(f"{name} local ")
    
Local()

print(f"{name} global")
'''



'''
name="codegnan"     #global
def Local():
    x=10     #local variable
    print(x)
    global name
    name="techgnan"
    print(f"{name} local ")
    
Local()

print(f"{name} global")
'''



'''
def Netflix(ruser,pin):
    username=input()
    password=int(input())
    if username==ruser and pin==password:
        def Inside(sub):
            if sub=="yes":
                print("this is inner function")
            else:
                print("no subscription")
            
        sub=input()
        result=Inside(sub)

    else:
        print("not found")
Netflix("john",12345)
'''



'''
def Purchase(amount,offer="no"):
    if offer=="yes":
        def Offer(discount):
            return amount-discount
        
        print(Offer(200))
    else:
        print(f"you have to pay {amount}")
        
    
amount=int(input())
offer=input()
Purchase(amount,offer)
'''




#pass by value and pass by referencr
'''
def Fun(x):
    x=20
    print(x)
    
    
y=int(input())
Fun=(y)
print(y)
'''



'''
def Fun(x):
    print(x)
    
    x.append(99)
    print(x)
    
    
y=[1,2,3,4]
Fun(y)

print(y)
'''



'''
def Fun(x):
    y=[7,8,9]
    print(y)
    
    
y=[1,2,3,4]
Fun(y)

print(y)
'''



'''
def Fun(x):
    x.append(99)
    print(x)
    
y=[1,2,3,4]
Fun(y)

print(y)
'''



'''
n = int(input())
a = 0
b = 1
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
'''



'''
n=5
a,b=0,1
for i in range(n):
    print(a)
    a,b=b,a+b
'''




