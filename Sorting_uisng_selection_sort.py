class Sorting:
    def __init__(self):
        self.list = []
    def add_data(self,data):
        self.list.append(data)
    def print_list(self):
        print("list = ",self.list)
    
    def selection_sort(self):
        n = len(self.list)
        for i in range(n):
            min_index = i
            for j in range(i+1,n):
                if self.list[j]<self.list[min_index]:
                    min_index = j
            self.list[i],self.list[min_index] = self.list[min_index],self.list[i]

                    




s= Sorting()
s.add_data(4)
s.add_data(5)
s.add_data(3)
s.add_data(1)
s.print_list()
s.selection_sort()

print("Aftaer sorting:",s.print_list())