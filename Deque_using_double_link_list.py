class Node:
    def __init__(self,item=None,prev=None,next=None):
        self.item=item
        self.prev=prev
        self.next=next

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count = 0

    def is_empty(self):
        return self.item_count == 0
    
    def insert_front(self, data):
        n = Node(data,None,self.front)
        if self.is_empty():
             self.rear = n
        else:
            self.front.prev = n
        self.front = n
        self.item_count += 1
    def insert_rear(self,data):
        n = Node(data,self.rear)
        if self.is_empty():
            self.front = n
        else:
            self.rear.next = n
        self.rear = n
        self.item_count+=1
    def delete_front(self):
        if not self.is_empty():
            if self.front == self.rear:
                self.front = None
                self.rear = None
                self.item_count-=1
            else:
                self.front = self.front.next
                self.front.prev = None
                self.item_count-=1
        else:
            raise IndexError("Deque is empty")
    def delete_rear(self):
        if not self.is_empty():
            if self.front == self.rear:
                self.front = None
                self.rear = None
                self.item_count-=1
            else:
                self.rear = self.rear.prev
                self.rear.next = None
                self.item_count-=1
        else:
            raise IndexError("Deque is empty")
    
    def get_front(self):
        if not self.is_empty():
            return self.front.item
        else:
            IndexError("Deque is empty")
    
    def get_rear(self):
        if not self.is_empty():
            return self.rear.item
        else:
            IndexError("Deque is empty")
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