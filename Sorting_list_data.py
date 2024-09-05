class Sorting:
    def __init__(self):
        self.list = []
    def add_data(self,data):
        self.list.append(data)
    def print_list(self):
        print("list = ",self.list)
    
    def sort(self):
        n = len(self.list)
        for i in range(n):
            for j in range(i+1,n):
                if self.list[i]>self.list[j]:
                    self.list[i],self.list[j] = self.list[j],self.list[i]



s= Sorting()
s.add_data(1)
s.add_data(4)
s.add_data(5)
s.add_data(3)
s.sort()
s.print_list()