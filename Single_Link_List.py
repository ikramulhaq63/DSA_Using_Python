######################## Singly Link List #################
# each node has a single node to a next node that why it is called a singly link list. each node only has one referance variable. it can grow and shrink.

#############Singly Link List Code##################
class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next

class SLL:
    def __init__(self, start=None): 
        self.start=start
    def is_empty(self):
        return self.start == None
    def insert_at_start(self,data):
        n=  Node(data, self.start)
        self.start = n
    def insert_at_last(self,data):
        n=Node(data)
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
        else:
            self.start = n
    def _search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None
    def insert_after(self,data, node):
        if node is not  None:
            n= Node(data, node.next)
            node.next = n
    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=" ")
            temp=temp.next    
    def delete_first(self):
        if self.start is not None:
            self.start=self.start.next
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None
    def delete_item(self,data):
        temp= self.start
        if self.start.next is None:
            pass
        elif self.start.next is None:
            if self.item == data:
                self.start.next = None
        else:
            temp=self.start
            if temp.item==data:
                self.start=temp.next
            while temp.next is not None:
                if temp.next.item==data:
                    temp.next=temp.next.next
                    break
                temp=temp.next



# mylist = SLL()
# mylist.insert_at_start(20)
# mylist.insert_at_last(45)
# mylist.insert_at_start(10)
# mylist.insert_after(4, mylist._search(20))
# mylist.delete_item(4)
# mylist.print_list( )