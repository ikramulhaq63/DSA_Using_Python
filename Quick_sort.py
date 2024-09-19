class Sorting:
    def __init__(self):
        self.list = []
    def add_data(self,data):
        self.list.append(data)
    def print_list(self):
        print("list = ",self.list)
    
    def quick_sort(self, data):
        if len(data)<=1:
            return data
        index_1 = data[0]
        lower_then_pivot_list = [x for x in data[1:] if x<index_1]
        greater_then_pivot_list = [x for x in data[1:] if x>index_1]
        return self.quick_sort(lower_then_pivot_list)+[index_1]+self.quick_sort(greater_then_pivot_list)
    def sort_and_print(self):
        self.list = self.quick_sort(self.list)
        print("After sorting........", self.list)
s= Sorting()
s.add_data(4)
s.add_data(5)
s.add_data(3)
s.add_data(1)
s.print_list()
s.sort_and_print()