'''
n=int(input())
x=n+10
if(x%2==0):
  print("even")
else:
  print("odd")
'''


#leap year
'''
year=int()
if (year%4==0 and year%100!=0) or year%400==0:
    print("leap year")
else:
     print("not")
'''





#cars needed:
'''
customers=int(input())
if customers%4==0:
    print(customers//4)
else:
    print(customers//4+1)
'''


#if,elif,else
'''
n = int(input())
if n == 0:
    print("zero")
elif n > 0:
    print("Positive")
else:
    print("Negative")
'''


#password:
'''
n = int(input())
if len(n) == 8:
    print("weak")
elif 1>8 and 1<16:
    print("good")
elif 1>15 and 1<=20:
     print("excellent")
elif 1>20:
    print("hard to remeber")
else:
    print("not valid")
 '''


#nested:
'''
username=input()
if username == "john":
    password=input()
    if password =="1234":
       print("login")
else:
    print("wrong username")
'''

#nested find std eligibility
'''
year=int(input("must be in [1,2,3,4]:"))
if year==4:
    marks=int(input())
    
    if marks>80 and marks<=100:
        backlogs=int(input())
        
        if backlogs!=0:
            print("not eligible must 0 backlogs")
        else:
            print("eligbile for training")

    else:
        print("marks must greater than 80")
else:
    print("year must be 4")
'''


#nested find std eligibility
'''
year=int(input("must be in [1,2,3,4]:"))
if year==4:
    marks=int(input("enter marks:"))
    
    if marks>80 and marks<=100:
        backlogs=int(input("enter bakclogs:"))
        
        if backlogs!=0:
            if backlogs>=1 and backlogs<=3:
                
                pay=input("you have to pay 5000 extra: [yes (or) no]:")
                if pay=="yes":
                    print("eligible for training")
                else:
                    print("must need to pay")

            elif backlogs>3:
                
                pay=input("you have to pay 10k [yes (or) no]:")
                if pay=="yes":
                    print("eligible for trainig")
                else:
                    print("must need to pay 10k")
                    
            
        else:
            print("eligbile for training")

    else:
        print("marks must greater than 80")
else:
    print("year must be 4")
'''    












