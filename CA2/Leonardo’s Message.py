pipe_num,shoe_num=map(int,(input().split()))
pipe_map=list(map(int,(input().split())))
for t in range(shoe_num):
    p,s=map(int,(input().split()))
    m=0
    while m in range(pipe_num):
        lost_f=0
        if pipe_map[m]<=p:
            m+=1
            continue
        
        else:
           
            count=0
            while True:
                if pipe_map[m]<=p:
                    count=0
                    break
                elif m==pipe_num:
                    lost_f=1
                    break
                elif count==s-1:
                
                    lost_f=1
                    break

                else:
                    count+=1
                    m+=1
                #print("problem!",count,m,lost_f)
            if lost_f:
                print("0")
                break 
    if lost_f==0:
        print("1")              



    
   