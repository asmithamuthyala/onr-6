'''
def Wish(name):
    print(f"{name} good morning . Your are the only one who completed the given task .. very good ma")
    
print(type(Wish))
'''



'''
def Addition(a,b,c):
    return a+b+c  #local
    print("slkjdflj")
    
x,y,z=map(int,input().split())  #global
print(Addition(x,y,z))  #None
'''



'''
def Find(l,search):
    for i in l:
        if search==i:
            return i
            
            
result=Find([1,2,3,4,5,1,1,1],1)
print(result+100)
'''



'''
def Stduents(name,marks,place="vijawada"): #defualt
    print(f"name:{name},marks:{marks},place:{place}")
    
    
Stduents("john",322) #positional

Stduents("sai",place="hyderbad",marks=678)  #keyword arguments
'''



'''
#calulator
def Cal(*Values):
    print(Values)
    print(sum(Values))
    
    
Cal(1,2,3)
Cal(1,2,3,4,5,7,8,8,7,77)
'''



'''
def Order(**items):
    print(items)
    
Order(chicken=1,briyani=2)
'''





