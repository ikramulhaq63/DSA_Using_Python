class Sorting:
    def __init__(self):
        self.list = []
    def add_data(self,data):
        self.list.append(data)
    def print_list(self):
        print("list = ",self.list)
    def final_merge(self,left,right):
        result = []
        i = j =0
        while i <len(left) and j <len(right):
            if left[i]<right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    def merge_sort(self, data):
        if len(data)<=1:
            return data
        Mid = len(data) // 2
        left =self.merge_sort (data[:Mid])
        right =self.merge_sort (data[Mid:])
        return self.final_merge(left,right)
    def sort_and_print(self):
        self.list = self.merge_sort(self.list)
        print("After sorting........", self.list)
s= Sorting()
s.add_data(4)
s.add_data(5)
s.add_data(3)
s.add_data(1)
s.print_list()
s.sort_and_print()