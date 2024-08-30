class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items)==0
    def push(self,data):
        self.items.append(data)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("stack is empty")
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")
    def size(self):
        return len(self.items)
    
o = Stack()
o.is_empty()
o.push(2)
o.push(6)
o.push(8)
print("The deleted element is",o.pop())
print("The last element of the stack is ",o.peek())
print("the size of the stack is ", o.size())