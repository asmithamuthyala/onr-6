'''
a=1
b=1
c=0
g=s=0
if a>g:
    g=a
    
if b>g:
    s,g=g,b
    
elif b>s and b!=g:
    s=b
    
if c>g:
    s,g=g,c
elif c>s and c!=g:
    s=c
print(g,s)
'''



'''
x=[10,1,2,9,7,8,6,10,11]
g=s=0
for i in x:
    if i>g:
        s,g=g,i
    elif i>s and i!=g:
        s=i
print(g,s)
'''


'''
for i in range(4):
    for j in range(68,68-i-1,-1):
        print(chr(j),end=" ")
    print()
'''


'''
for i in range(68,64,-1):
    for j in range(68,i-1,-1):
        print(chr(j),end=" ")
    print()
'''



'''
for i in range(5):
    for j in range(5):
        if i==0 or j==0 or i==4 or j==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''



