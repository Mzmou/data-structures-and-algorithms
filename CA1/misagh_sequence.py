series=(input())
a1=a2=a3=""
step1=step2=step3=1
i=j=k=0
for i in range(len(series)):
    step3=step2=1
    a1=series[0:step1]
    j=step1
    i+=step1
    step1+=1   
    if j+step2>len(series):
        break
    while j+step2<=len(series):
        if series[j]=="0":
            break
        a2=series[j:j+step2]
        a3=str(int(a1)+int(a2))
        step3=len(a3)
        k=j+step2
        step2+=1
        if k+step3>len(series):
            break
        while k+step3<=len(series):
            temp=series[k:k+step3]
            if temp==a3:
                a1=a2
                a2=a3
                a3=str(int(a1)+int(a2))
                if k+step3==len(series):
                    print("YES")
                    exit()
                k+=step3    
                step3=len(str(int(a1)+int(a2)))
            else:
                a1=series[0:step1-1]
                
                break    
           
print("NO")


