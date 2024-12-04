num_of_sessions=int(input())
str_list_list=[]
for i in range(num_of_sessions):
    temp=""
    num,time=input().split()
    hour,minute=map(int,num.split(":"))
    if time=="PM" and hour!=12:
        hour+=12
    if time=="AM" and hour==12:
        hour-=12    
    num_of_friends=int(input())
    str_list=[]
    for j in range(num_of_friends):
        num1,time1,num2,time2=input().split() 
        hour1,minute1=map(int,(num1.split(":"))) 
        hour2,minute2=map(int,(num2.split(":")))
        if time1=="PM" and hour1!=12:
            hour1+=12
        if time2=="PM" and hour2!=12:
            hour2+=12
        if time1=="AM" and hour1==12:
            hour1-=12 
        if time2=="AM" and hour2==12:
            hour2-=12      
        if hour>hour1 and hour<hour2:
            temp=temp+"1"
            #print(1,end="")         
        elif hour==hour1 and hour!=hour2 and minute>=minute1:
             temp=temp+"1"
            #print(1,end="")
        elif hour==hour2 and hour!=hour1 and minute<=minute2:
             temp=temp+"1"
           # print(1,end="") 
        elif hour==hour2==hour1 and minute>=minute1 and minute<=minute2:
             temp=temp+"1"  
        else:
             temp=temp+"0"
        if j==num_of_friends-1:
            str_list_list.append(temp)             
for t in str_list_list:
    print(t)          
        