
nodes_num,query_num=map(int,input().split())
nodes_list=list(map(int,input().split()))
nodes_map=[-1]+nodes_list
nodes_set={}
for i in range(len(nodes_map)):

    nodes_set.setdefault(i+1,set())
for i in range(len(nodes_map)):

    if nodes_map[i] == -1:
        root = i+1

    else:

        nodes_set[nodes_map[i]].add(i+1)
steps_arr=[]
for i in range(query_num):
    steps=0
    marked_nodes=list(map(int,input().split()))
    marked_nodes=marked_nodes[1:]
    pch_set=set(marked_nodes) 
    for m_e in  (marked_nodes):
        papa=nodes_map[m_e-1]
        children=(nodes_set[m_e])
        steps+=len(children)-len(children.intersection(pch_set))
        if papa not in pch_set:
           steps+=1
       
    steps_arr.append(steps)    
            
        
        
print(*steps_arr,sep='\n')
            
#print(-1)    
    