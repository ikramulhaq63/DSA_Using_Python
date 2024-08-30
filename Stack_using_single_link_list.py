class Node:
    def __init__(self,item,next):
        self.item = item
        self.next = next
class Stack:
    def __init__(self):
        self.start = None
        self.item_count=0

    def is_empty(self):
        return self.start==None
    
    def push(self,data):
        n=Node(data,self.start)
        self.start = n
        self.item_count+=1
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is already empty")
        else:
            data = self.start.item
            self.start = self.start.next
            self.item_count-=1
            return data

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        else:
            data=self.start.item
            return data
    def size(self):
        return self.item_count
    
object = Stack()
object.push(4)
object.push(5)
object.push(6)       
print("deleted item is ",object.pop())
print("top element of the stack is ",object.peek())
print("size of the stack is ",object.size())