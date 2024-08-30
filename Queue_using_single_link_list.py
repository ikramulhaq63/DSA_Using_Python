class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count = 0

    def is_empty(self):
        return self.front == None
    
    def enqueue (self,data):
        if not self.is_empty():
            n= Node(data)
            self.rear.next = n
            self.rear = n
            self.item_count+=1
        else:
            n = Node(data)
            self.front = n
            self.rear = n
            self.item_count+=1
    def dequeue(self):
        if not self.is_empty():
            removed_item=self.front.item
            self.front = self.front.next
            self.item_count-=1
            return removed_item
        else:
            raise IndexError("Queue is empty")
    def get_front(self):
        if not self.is_empty():
            return self.front.item
        else:
            raise IndexError("Queue is empty")
    
    def get_rear(self):
        if not self.is_empty():
            return self.rear.item
        else:
            raise IndexError("Queue is empty")

    def size(self):
        return self.item_count
    
o = Queue()
o.enqueue(1)
o.enqueue(2)
o.enqueue(3)
o.enqueue(4)
o.enqueue(5)
o.enqueue(6)
o.enqueue(7)
o.enqueue(8)
print("The deleted element is",o.dequeue())
print("The rare element of the stack is ",o.get_rear())
print("The front element of the stack is ",o.get_front())
print("the size of the stack is ", o.size())