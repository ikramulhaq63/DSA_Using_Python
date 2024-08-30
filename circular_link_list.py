class Node:
    def __init__(self,item=None,next=None):
        self.next=next
        self.item= item

class CLL:
    def __init__(self):
        self.last=None

    def is_empty(self):
        return self.last==None
    def insert_at_start(self,data):
        n = Node(data)
        if self.last is not None:
            n.next = self.last.next
            self.last.next = n
        else:
            n.next=n
            self.last=n
    def insert_at_last(self,data):
        n = Node(data)
        if self.last is not None:
            n.next=self.last.next
            self.last.next = n
            self.last = n
            
        else:
            self.last = n
            n.next=n
    def search(self,data):
        if self.last is not None:
            temp = self.last.next
            while temp!=self.last:
                if temp.item == data:
                    return temp
                temp = temp.next
            if temp.item == data:
                return data
            return None
        else:
            return None
    def insert_after(self,temp,data):
        if temp is not None:
        
            n=Node(data,temp.next)
            temp.next=n
            if temp == self.last:
                self.last = n
    def print_list(self):
        if not self.is_empty():
            temp = self.last.next
            while temp!=self.last:
                print(temp.item, end=" ")
                temp = temp.next
            print(temp.item)
    
    def delete_first(self):
        if self.last is not None:
            if self.last.next==self.last:
                self.last ==None
            else:
                self.last.next = self.last.next.next
    
    def delete_last(self):
        if self.last is  not None:
            if self.last.next==self.last:
                self.last=None
            else:
                temp = self.last.next
                while temp.next!=self.last:

                    temp=temp.next
                temp.next =self.last.next
                self.last = temp
            
    def delete_item(self,data):
        if self.last is not None:
            if self.last.next==self.last:
                if self.last.item == data:
                    self.last = None
            else:
                if self.last.next.item == data:
                    self.delete_first()
                else:
                    temp = self.last.next
                    while temp!=self.last:
                        if temp.next == self.last:
                            if self.last.item == data:
                                self.delete_last()
                        if temp.next.item == data:
                            temp.next=temp.next.next
                            break
                        temp=temp.next

o = CLL()
o.insert_at_start(1)
o.insert_at_last(2)
o.print_list()
