class Bst:
    class Node:
        def __init__(self,val):
            self.val=val
            self.right=None
            self.left=None
            self.parent=None
            self.index=None
            pass

    def __init__(self):
        self.root=None
        self.size=0

        pass
    def search(self,key,root,parent):
        if self.size==0:
            return None
        if not root:
            return parent
        elif key>=root.val:
            return self.search(key,root.right,root)
        else:
            return self.search(key,root.left,root)
    
    
    def insert(self, key,index):
        insert_loc=self.search(key,self.root,None)
        #print("hii")
        self.size+=1
        if insert_loc==None:
            self.root=self.Node(key)
            self.root.index=index
            self.root.parent=None
            
            #print(self.root.val)
        else:
            if key>=insert_loc.val:
                insert_loc.right=self.Node(key) 

                insert_loc.right.parent=insert_loc
                insert_loc.right.index=index
                print(insert_loc.right.parent.val,end=" ")
                return insert_loc.right
            else:
                insert_loc.left=self.Node(key)  
                insert_loc.left.parent=insert_loc
                insert_loc.left.index=index
                print(insert_loc.left.parent.val,end=" ")
                return insert_loc.left


        
        
    

        
    
    def inorder(self):
        current=self.root
        stack=[]

        while True:
            if current!=None:
                #print(current.val)
                stack.append(current)
                current = current.left
            elif len(stack)>0:
                current=stack.pop() 
                print(current.val,end=" ") 
                current=current.right  
            else:
                break   


num= int(input())
tree_elements=list(map(int,input().split()))
indexes=list(map(int,input().split()))


bst=Bst()
x1,x2=None,None
for i in range(num):
    t=bst.insert(tree_elements[i],i+1)
    
    if i==indexes[0]-1:
        x1=t
    if i==indexes[1]-1:
        x2=t    
print()        
#print(x1.parent.val,x2.parent.val)    
stack1=[]
stack2=[]
parent=x1.parent
while parent!=None:
    stack1.append([(parent.val),parent.index])
    parent=parent.parent
parent=x2.parent
while parent!=None:
    stack2.append([(parent.val),parent.index])
    parent=parent.parent    
min_stack=[]
max_stack=[]
if len(stack1)<len(stack2):
    min_stack=stack1
    max_stack=stack2
else :
    max_stack=stack1
    min_stack=stack2
i=0
j=0   
if indexes[0]==indexes[1]:
    print(indexes[0])
    exit ()
for i in range(len(min_stack)):
    if min_stack[i] in max_stack:
        print(min_stack[i][1])
        break
      













