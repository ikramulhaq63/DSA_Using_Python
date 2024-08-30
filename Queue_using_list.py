class Queue:
    def __init__(self):
        self.items = []
        self.item_count=0

    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue (self,data):
        self.items.append(data)
        self.item_count+=1
    
    def dequeue(self):
        if not self.is_empty():
            self.item_count-=1
            return self.items.pop(0)
        else:
            raise IndexError("Queue is already empty")
    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")
    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Queue is empty")
    def size(self):
        return self.item_count
    
o = Queue()
o.enqueue(2)
o.enqueue(6)
o.enqueue(8)
print("The deleted element is",o.dequeue())
print("The last element of the stack is ",o.get_rear())
print("The First element of the stack is ",o.get_front())
print("the size of the stack is ", o.size())

