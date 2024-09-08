class Sorting:
    def __init__(self):
        self.list = []
    def add_data(self,data):
        self.list.append(data)
    def print_list(self):
        print("list = ",self.list)
    
    def Insertion_sort(self):
        n = len(self.list)
        for i in range(1,n):
            key = self.list[i]
            for j in range(i-1,-1,-1):
                if self.list[j]>key:
                    self.list[j+1] = self.list[j]
                else:
                    self.list[j+1] =key
                    break
            else:
                self.list[0] = key

s= Sorting()
s.add_data(4)
s.add_data(5)
s.add_data(3)
s.add_data(1)
s.print_list()
s.Insertion_sort()

print("Aftaer sorting:",s.print_list())