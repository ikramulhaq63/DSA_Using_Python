
class Deque:
    def __init__(self):
        self.items = []
        self.item_count = 0

    def is_empty(self):
        return  len(self.items) == 0
        
    def insert_front(self,data):
            self.items.insert(0,data)
            self.item_count+=1

    def insert_rear(self,data):
        self.items.append(data)
        self.item_count+=1
    def delete_front(self):
        if not self.is_empty():
            removed_item = self.items[0]
            self.items.pop(0)
            self.item_count-=1
            return removed_item
        else:
            raise IndexError("Deque is empty")
    def delete_rear(self):
        if not self.is_empty():
            removed_item = self.items[-1]
            self.items.pop()
            self.item_count-=1
            return removed_item
        else:
            raise IndexError("Deque is empty")
    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Deque is empty")
    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Deque is empty")
    def size(self):
        return self.item_count

o = Deque()
o.insert_front(10)
o.insert_front(20)
o.insert_rear(30)
o.insert_rear(40)
# print("The deleted front element is: ",o.delete_front())
# print("The deleted rear element is: ",o.delete_rear())
print("The front element of the stack is ",o.get_front())
print("The rare element of the stack is ",o.get_rear())
print("the size of the stack is ", o.size())