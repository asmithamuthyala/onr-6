'''
def Score_board(overs):
    l=[];start=1
    while start<=overs:
        balls=1
        while balls<=6:
            ball_score=input(f"enter over {start} ball:{balls}:")
            if ball_score=="wd" or ball_score=="nb":
                l.append(1)
                continue
            else:
                l.append(ball_score)
                balls+=1
        print(l)
        start+=1
    
Score_board(2)
'''




#x=[1,2,3,4,5,6]
#print(len(x))

def Length(x):
    count=0
    for i in x:
        count+=1
        return count
        
print(Length([1,2,3]))        