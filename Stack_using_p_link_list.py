from Single_Link_List import *
class Stack:
    def __init__(self):
        self.mylist=SLL()
        self.item_count = 0
    def is_empty(self):
        return self.mylist.is_empty()
    def push(self,data):
        self.mylist.insert_at_start(data)
        self.item_count+=1
    def pop(self):
        if not self.is_empty():
            self.mylist.delete_first()
            self.item_count-=1
    def peek(self):
        if not self.is_empty():
            return self.mylist.start.item
    def size(self):
        return self.item_count

object = Stack()
object.push(4)
object.push(5)
object.push(6)       
print("deleted item is ",object.pop())
print("top element of the stack is ",object.peek())
print("size of the stack is ",object.size())