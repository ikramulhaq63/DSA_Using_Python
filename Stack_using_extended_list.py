class Stack(list):
    def is_empty(self):
        return len(self)==0
    def push(self,data):
        self.append(data)
    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError("stack is already empty")
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("stack is empty")
    def size(self):
        return len(self)
    def insert(self ,index,data):
        raise AttributeError ("you can not enter data in this list because it ia an stack")
    
object = Stack()
object.push(4)
object.push(7)
object.push(8)
print("deleted item from the stack is ",object.pop())
print("last element in the stack is ", object.peek())
print("size of the stack is ",object.size())