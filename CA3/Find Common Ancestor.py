import heapq
n,d=map(int,(input().split()))
heap3=[]
heap_sort=[]
max_anger=0
for i in range(n):
    a,t,s=map(int,(input().split()))
    heap_sort.append([a,t,s])
    max_anger+=t*s
heap_sort.sort(key=lambda x: x[0])
  
j=0   
flag=0
for i in range(d):
    flag=0
    while j<n and heap_sort[j][0]==i+1:
         heapq.heappush(heap3,(-heap_sort[j][2],heap_sort[j]))
         j+=1
        

    if len(heap3)!=0:
      max_anger-=heap3[0][1][2]
      heap3[0][1][1]-=1
      if heap3[0][1][1]==0:
         heapq.heappop(heap3)
    
            
           
        
 
print(max_anger)           



    