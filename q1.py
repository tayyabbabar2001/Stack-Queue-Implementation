class Stack():
    def __init__(self, size):
        self.size = size
        self.stack = []
    
    def push (self, data):
        if len(self.stack) == self.size:
            print("Stack is at maximum capacity")
        else:
            self.stack.append(data)

    def pop (self):
        return self.stack.pop()
        self.stack.pop()
    
    def gettop():
        return self.stack[-1]
        self.stack.pop()

    def isEmpty (self):
        if len(self.stack)==0:
            print("Stack is empty")
        else:
            print("Stack is not empty")
        
    def isFull (self):
        if len(self.stack)==0:
            return True
        else:
            return False
     
    def getsize(self):
        #print (len(self.stack))
        return len(self.stack)
    
    def printstack(self):
        print(self.stack)
    
def stack():
        mystack= Stack(4)
        mystack.push("Tayyab")
        mystack.push("Babar")
        mystack.push("TB")
        mystack.printstack()
        mystack.pop()
        mystack.getsize()
        mystack.printstack()
stack()    

#task 2
class Queue:
    def __init__(self,size):
        self.size = size
        self.queue= []

    def enqueue(self,data):
        if len(self.queue)== self.size:
            print("Queue is at max capacity")
        else:
            self.queue.append(data)
    
    def dequeue(self):
        if len(self.queue)!=0:
            return self.queue.pop(0)
    
    def front(self):
        return self.queue[0]
    
    def isEmpty(self):
        if len(self.queue)==0:
            print("Queue is empty")
        else:
            print("Queue is not empty")

    def isFull (self):
        if len(self.queue)==self.size:
            print("queue is full")
        else:
            print("Queue is not empty")

    def GetSize(self):
        return len(self.queue)
    
    def printqueue(self):
        print (self.queue)

def que():
        myque=Queue(5)
        myque.enqueue("T")
        myque.enqueue("B")
        myque.enqueue("TB")
        myque.printqueue()
        myque.dequeue()
        myque.enqueue("T")
        myque.enqueue("B")
        myque.printqueue()
        
que()

def stack():
    mystack1 = Stack(4)
    mystack2 = Stack(4)

    mystack1.push(1)
    mystack1.push(2)
    mystack1.push(3)

    mystack2.push(mystack1.pop())
    mystack2.push(mystack1.pop())
    mystack2.push(mystack1.pop())
    mystack2.printstack()
stack()
    
class Stack():
    def sort_stack(stack):
        sorted_stack = Stack(stack.size) 
    while not stack.isEmpty():
        temp = stack.pop()
        while not sorted_stack.isEmpty() and sorted_stack.gettop() > temp:
            stack.push(sorted_stack.pop())
        sorted_stack.push(temp)
    return sort_stack

def stack_sort_example():
    mystack = Stack(4)
    mystack.push(4)
    mystack.push(1)
    mystack.push(3)
    mystack.push(2)

    print("Original stack:")
    mystack.printstack()

    sorted_stack = sort_stack(mystack)

    print("Sorted stack:")
    sorted_stack.printstack()

stack_sort_example()