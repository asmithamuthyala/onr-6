'''
def Hello():
    print("hii")
    
    Hello()
    
Hello()
'''



'''
def Number(n):
    if n==10:
        return
    
    else:
        print(n)
        Number(n+1)
Number(1)        
'''



def Fact(n):
    if n==5:
        return 5
    
    else:
        return n*Fact(n+1)
        
print(Fact(1))        

        
        
        