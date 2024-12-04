
size = int(input())
paint = list()

for i in range(size):
    paint.append(int(input()))
map_c = {}
prev_colors = list()
for i in set(paint):
    map_c[i] = []

for i in range(size):
    map_c[paint[i]].append(i)


stack = list()
max_size = 0
max_arr=[]

for i in range(size):
    if paint[i]==0:
        continue
    if map_c[paint[i]].__len__()==1:
        max_size+=1
        max_arr.append(max_size)
        max_size-=1
    elif map_c[paint[i]].__len__()>1 and i==map_c[paint[i]][0]:
        max_size+=1
        max_arr.append(max_size)  
    elif  map_c[paint[i]].__len__()>1 and i==map_c[paint[i]][-1]   and i!=0 and  len(map_c[paint[i-1]])>=2 and (i-1)!=map_c[paint[i-1]][-1] and i!=(size-1) and paint[i]!=paint[i-1]:
        #print(paint[i],i)
        print(-1)
        exit(0)
    elif  map_c[paint[i]].__len__()>1 and i==map_c[paint[i]][-1] :
   
        max_size-=1     
        max_arr.append(max_size)
print(max(max_arr))       
        