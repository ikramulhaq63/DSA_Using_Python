class Sorting:
    def __init__(self):
        self.list = []
    def add_data(self,data):
        self.list.append(data)
    def print_list(self):
        print("list = ",self.list)
    def heepifing(self,data,n,i):
        node_wo_leaf = i
        left_child = 2*i+1
        right_child = 2*i+2
        if right_child <n and data[right_child]>data[node_wo_leaf]:
            node_wo_leaf =right_child
        if left_child<n and data[left_child]>data[node_wo_leaf]:
            node_wo_leaf =left_child
        if node_wo_leaf != i:
            data[i], data[node_wo_leaf] = data[node_wo_leaf],data[i]
            self.heepifing(data,n,node_wo_leaf)
    def heep(self, data):
        n = len(data)
        for i in range(n//2-1,-1,-1):
            self.heepifing(data,n,i)
        print("After heepifing........", self.list)
        for i in range(n-1,0,-1):
            data[0],data[i] = data[i],data[0]
            self.heepifing(data,i,0)
        return data
    def sort_and_print(self):
        self.list = self.heep(self.list)
        print("After sorting........", self.list)
s= Sorting()
s.add_data(4)
s.add_data(9)
s.add_data(10)
s.add_data(98)
s.add_data(7)
s.add_data(76)
s.add_data(45)
s.add_data(3)
s.add_data(1)
s.print_list()
s.sort_and_print()