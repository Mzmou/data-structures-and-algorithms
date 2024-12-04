layers=input()
dict_ham={}
length=max_len=0
for i in range(layers.__len__()):
    if layers[i] in dict_ham:
        index=dict_ham[layers[i]]
        del_items=0
        for v in list(dict_ham.keys()):
            if dict_ham[v]<=index:
                del dict_ham[v]
                del_items+=1
        
        length-=del_items
       

    dict_ham.setdefault(layers[i],i) 
    length+=1 
    #print(dict_ham)  
    max_len=max(max_len,length)
print(max_len)        




