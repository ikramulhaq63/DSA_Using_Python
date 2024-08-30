class Node:
    def __init__(self, item=None, priority=None, next=None):
        self.items = item
        self.priority = priority
        self.next = next
    
class PriorityQueue:
    def __init__(self):
        self.start = None
        self.item_count = 0
    
    def is_empty(self):
        return self.start is None

    def push(self, data, p_number):
        n = Node(data, p_number)
        # Case 1: If the queue is empty or the new node has the highest priority (i.e., smallest priority number)
        if not self.start or p_number < self.start.priority:
            n.next = self.start
            self.start = n
        else:
            # Traverse the list to find the correct position to insert the new node
            temp = self.start
            while temp.next and temp.next.priority <= p_number:
                temp = temp.next
            
            # Insert the new node after `temp`
            n.next = temp.next
            temp.next = n
            
        self.item_count += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Priority queue is already empty")
        else:
            data = self.start.items
            self.start = self.start.next
            self.item_count -= 1
            return data
    
    def size(self):
        return self.item_count

# Example usage
o = PriorityQueue()
o.push("Amit", 4)
o.push("Arjun", 7)
o.push("Ashime", 2)
o.push("Agrah", 5)
o.push("Anant", 8)
o.push("Ambike", 1)
while not o.is_empty():
    print(o.pop())
print("Size of the queue is:", o.size())

