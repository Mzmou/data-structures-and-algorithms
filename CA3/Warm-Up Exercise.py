from ast import While
from platform import node
from queue import Empty
import select
import sys
import re
from tkinter import NO
#from typing import Self
#from typing import Self
from xml.dom import Node


INVALID_INDEX = 'invalid index'
OUT_OF_RANGE_INDEX = 'out of range index'
EMPTY = 'empty'


class MinHeap:
    class Node:
        def __init__(self,val):
            self.val = val
        pass

    def __init__(self):
        self.heap=[]
     

        pass

    def bubble_up(self, index):
        self.exeption(index)
        while index >0:
            dad=None
            dad_index=int((index-1)/2)
            child=self.heap[index].val
            if dad_index>=0:
                dad=self.heap[dad_index].val
            if dad!=None and dad>child:
                self.heap[dad_index].val,self.heap[index].val=self.heap[index].val,self.heap[dad_index].val
            else: 
                break
            index=dad_index

        pass

    def bubble_down(self, index):
        self.exeption(index)
        min=index
        while 2*index < len(self.heap):
            children1=None
            children2=None
            #print('he',index)
            if 2*index+1 < len(self.heap):
                #print(index,"1")
                children1= self.heap[2*index+1].val
            if 2*index+2 < len(self.heap):
                #print(index,"2")
                children2=self.heap[2*index+2].val
            if children2!=None and children2<self.heap[min].val:

                min=2*index+2  
            if children1!=None and children1<self.heap[min].val:

                min=2*index+1   
            if min != index:

                self.heap[min].val,self.heap[index].val=self.heap[index].val,self.heap[min].val
                index = min
            else: break


        pass

    def heap_push(self, value):
        self.heap.append(self.Node(value))

        self.bubble_up(len(self.heap)-1)
        pass

    def heap_pop(self):
        self.exeption("poping_index")
        popped_element=self.heap[0].val
        self.heap[0]=self.heap[len(self.heap)-1]
        self.heap.pop()

        if len(self.heap)>0:
            self.bubble_down(0)
        return popped_element
    def exeption(self,index):
        if index=="poping_index":
            if len(self.heap)==0:
                raise Exception(EMPTY)
            return

        if not isinstance(index, int):
            raise Exception(INVALID_INDEX)
        if index<0 or index>=len(self.heap):
            raise Exception(OUT_OF_RANGE_INDEX)
        if len(self.heap)==0:
            raise Exception(EMPTY)

    def find_min_child(self, index):

        self.exeption(index)

        children=[]
      
        if 2*index<len(self.heap):
            children.append(self.heap[2*index+2].val)
            children.append(self.heap[2*index+1].val)

        if children[1]>children[0]:
            return 2*index+2
        else:
            return 2*index+1


    def heapify(self, *args):
        for i in range(len(args)):
            self.heap_push(args[i])
        pass


class HuffmanTree:
    class Node:
        def __init__(self,repetition,letter) -> None:
            self.letter=letter

            self.freg=repetition
            self.num=""
            self.right=None
            self.left=None

            
        pass

    def __init__(self):
        self.letters=[]
        self.repetition=[]
        self.dict=[]
        self.result=""
        self.dict_enc={}
        self.root=""
        pass

    def set_letters(self, *args):
        self.letters=args
        pass

    def set_repetitions(self, *args):
        self.repetition=args
        pass
    def set_tree_dict(self):

        for i in range(len(self.letters)):
            self.dict.append(self.Node(self.repetition[i],self.letters[i]))
    def encode(self,node,sum):
        sum=str(node.num)+sum
        if node.right!=None:
            self.encode(node.right,sum)
        if node.left!=None:
            self.encode(node.left,sum)
        if node.left==None and node.right==None:
            self.dict_enc.setdefault(node.letter,sum)        

    def build_huffman_tree(self):

        self.set_tree_dict()
        while len(self.dict)>1:
            self.dict = sorted(self.dict, key=lambda x: x.freg)
            node1=self.dict[0]
            node1.num=0
            node2=self.dict[1]
            node2.num=1
            node3=self.Node(node1.freg+node2.freg,"defualt")
            node3.right=node2
            node3.left=node1
            self.dict.pop(0)
            self.dict.pop(0)
            self.dict.append(node3)
            self.root=node3
        self.encode(self.root,"")


        pass

    def get_huffman_code_cost(self):
        result=0
        for i in range(len(self.letters)):
            result+=len(self.dict_enc[self.letters[i]])*(self.repetition[i])
        return result    

            
        pass

    def text_encoding(self, text):
        dict_letters={}
        for i in text:
            if i not in dict_letters:
                dict_letters.setdefault(i,0)
            dict_letters[i]+=1
       
        self.letters=list(dict_letters.keys())
        self.repetition=list(dict_letters.values())


        self.build_huffman_tree()            
                

        


class Bst:
    class Node:
        def __init__(self,val):
            self.val=val
            self.right=None
            self.left=None
            self.parent=None
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
    
    
    def insert(self, key):
        insert_loc=self.search(key,self.root,None)
        #print("hii")
        if insert_loc==None:
            self.root=self.Node(key)
            self.root.parent=None
            
            #print(self.root.val)
        else:
            if key>=insert_loc.val:
                insert_loc.right=self.Node(key) 
                #print(key)
                insert_loc.right.parent=insert_loc
                #print(insert_loc.right.parent.val)
            else:
                insert_loc.left=self.Node(key)  
                insert_loc.left.parent=insert_loc
                #print(insert_loc.left.parent.val)

        self.size+=1
    

        
    
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
        
        #pass


class Runner:
    dsMap = {'min_heap': MinHeap, 'bst': Bst, 'huffman_tree': HuffmanTree}
    callRegex = re.compile(r'^(\w+)\.(\w+)\(([\w, \-"\']*)\)$')

    def __init__(self, inputSrc):
        self.input = inputSrc
        self.items = {}

    def run(self):
        for line in self.input:
            line = line.strip()
            action, _, param = line.partition(' ')
            actionMethod = getattr(self, action, None)
            if actionMethod is None:
                return
            actionMethod(param)

    def make(self, params):
        itemType, itemName = params.split()
        self.items[itemName] = self.dsMap[itemType]()

    def call(self, params):
        regexRes = self.callRegex.match(params)
        itemName, funcName, argsList = regexRes.groups()

        args = [x.strip() for x in argsList.split(',')] if argsList != '' else []
        args = [x[1:-1] if x[0] in ('"', "'") else int(x) for x in args]

        method = getattr(self.items[itemName], funcName)
        try:
            result = method(*args)
        except Exception as ex:
            print(ex)
        else:
            if result is not None:
                print(result)


def main():
    #runner = Runner(sys.stdin.readline)
    runner = Runner(sys.stdin)
    runner.run()


if __name__ == "__main__":
    main()
