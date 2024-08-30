class PriorityQueue:
    def __init__(self):
        self.items = []
        self.item_count = 0
    def push(self,data,p_number):
        index = 0
        while index < len(self.items) and self.items[index][1]<=p_number:
            index =index+1
        self.items.insert(index,(data,p_number))
        self.item_count+=1
    def is_empty(self):
        return len(self.items) == 0
    
    def pop(self):
        # if self.is_empty():
        #     raise IndexError("Priority Queue is already emopty")
        # else:    
        #     index = 0
        #     for i in range(1,len(self.items)):
        #         if self.items[i][1]< self.items[index][1]:
        #             index =i
        #     self.items.pop(index)
        if self.is_empty():
            raise IndexError("Priority queue is already empty empty")
        else:
            self.item_count-=1
            return self.items.pop(0)[0]
    
    def size(self):
        return self.item_count

o = PriorityQueue()
o.push(2,6)
o.push(2,7)
print("delete item is ",o.pop())
o.size()