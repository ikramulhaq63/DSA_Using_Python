from Single_Link_List import *

class Stack(SLL):
    def __init__(self):
        super().__init__()
        self.item_count = 0
    def is_empty(self):
        return super().is_empty()
    
    def push(self,data):
        super().insert_at_start(data)
        self.item_count+=1
    def insert_after(self, data, node):
        raise AttributeError ("you can not enter data in this list because it ia an stack")
    def insert_at_last(self, data):
        raise AttributeError ("you can not enter data in this list because it ia an stack")
    def pop(self):
        if not self.is_empty():
            self.item_count-=1
            return super().delete_first()
        else:
            raise AttributeError("Stack is already empty")
    def delete_item(self, data):
        raise AttributeError ("you can not delete specific data in this list because it ia an stack")
    def delete_last(self):
        raise AttributeError ("you can not delete specific data in this list because it ia an stack")
    
    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise AttributeError("Stack is empty so you can not view the first element")
    
    def size(self):
        return self.item_count

object = Stack()
object.push(4)
object.push(5)
object.push(6)  
object.pop()     
print("top element of the stack is ",object.peek())
print("size of the stack is ",object.size())