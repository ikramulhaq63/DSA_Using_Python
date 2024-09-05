class Sorting:
    def __init__(self):
        self.list = []
    def add_data(self,data):
        self.list.append(data)
    def print_list(self):
        print("list = ",self.list)
    
    def bubble_sort(self):
        n = len(self.list)
        for i in range(n):
            swapped = False
            for j in range(0,n-i-1):
                if self.list[j]>self.list[j+1]:
                    self.list[j],self.list[j+1] = self.list[j+1],self.list[j]
                    swapped = True
            if not swapped:
                break





s= Sorting()
s.add_data(1)
s.add_data(4)
s.add_data(5)
s.add_data(3)
s.bubble_sort()
s.print_list()