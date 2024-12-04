import sys
import re
import copy

class Queue:
    def __init__(self):
        self.q=LinkedList()
        self.size=0
        pass

    def getSize(self):
        return self.size
        pass

    def enqueue(self, value):
        self.q.insertEnd(value)
        self.size+=1
        pass

    def dequeue(self):
        val=self.q.head.value
        self.q.head=self.q.head.next
        
        self.size-=1
        return(val)
        pass

    def isEmpty(self):
        if self.size==0:
            return True
        else:
            return False
        pass

    def getInOneLine(self):
        self.q.getList()
        pass


class Stack:
    def __init__(self, size=10):
        self.size=0
        self.st=LinkedList()
        self.capacity=10
        pass

    def isEmpty(self):
        if self.size:
            return False
        else:
            return True 
        pass

    def push(self, value):
        self.st.insertFront(value)
        self.size+=1


        pass

    def pop(self):
        val=self.st.head.value
        self.st.head=self.st.head.next
        self.size-=1
        print(val)
        pass

    def put(self, value):
        self.st.head.value=value
        pass

    def peek(self):
        return self.st.head.value
        pass

    def expand(self):
        self.capacity*=2
        pass

    def getInOneLine(self):
        self.st.reverse()
        self.st.getList()
        self.st.reverse()
        pass

    def getSize(self):
        return self.size
        pass

    def getCapacity(self):
        return self.capacity
        pass


class Node:
    def __init__(self, val):
        self.value=val
        self.next=None
        
        pass


class LinkedList:
    def __init__(self):
        self.head=None

        pass

    def getList(self):
        list_linked=[]
        it=self.head

        while it!=None:
            list_linked.append(it.value)
            it=it.next
        print(*list_linked)    
        pass

    def insertFront(self, new_data):
        new_node=Node(new_data)
        if self.head==None:
          
            self.head=new_node
            new_node.next=None
        else:
            new_node.next=self.head   
            self.head=new_node 


        pass

    def insertEnd(self, new_data):
        if self.head!=None:
            next_node=self.head
            while True:
                if next_node.next==None:
                    break
                next_node=next_node.next
            next_node.next=Node(new_data)
            next_node.next.next=None
        else:
            self.head=Node(new_data)
            self.head.next=None

        pass

    def reverse(self):
        prev=None
        it=self.head
        next=it.next
        while it!=None:
            next=it.next
            if next==None:
                self.head=it

            it.next=prev
            prev=it
            it=next
        pass
    


class Runner:
    dsMap = {'stack': Stack, 'queue': Queue, 'linked_list': LinkedList}
    callRegex = re.compile(r'^(\w+)\.(\w+)\(([\w, ]*)\)$')

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
        args = argsList.split(',') if argsList != '' else []

        method = getattr(self.items[itemName], funcName)
        result = method(*args)
        if result is not None:
            print(result)


def main():
    runner = Runner(sys.stdin)
    runner.run()


if __name__ == "__main__":
    main()
