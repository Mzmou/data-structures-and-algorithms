word=input()
bit_map="0000000000"
dict={"0000000000":1}
answer=0
for i in range(len(word)):
    index=ord(word[i])-97
    #bit_map[index]=str(not int(bit_map[index]))
    bit_map=bit_map[:index]+str(int(not int(bit_map[index])))+bit_map[index+1:]
    #print(bit_map)
    if bit_map in dict:
        answer+=dict[bit_map]
        dict[bit_map]+=1
    else:
        dict.setdefault(bit_map,1)    
    for j in range(10):
       temp=bit_map[:j]+str(int(not  int(bit_map[j])))+bit_map[j+1:]
       if temp in dict:
            answer+=dict[temp]
       else: 
           dict.setdefault(temp,0)     
       
print(answer) 
    

        
           