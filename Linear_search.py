class Sorting:
    def __init__(self):
        self.list = []
    def add_data(self,data):
        self.list.append(data)
    def print_list(self):
        print("list = ",self.list)
    def Linear_search(self, data,item):
        if data is not None:
            for i in data:
                if i == item:
                    return i

        
    def Search_and_print(self,item):
        self.list = self.Linear_search(self.list,item)
        print("Your search value is ........", self.list)
s= Sorting()
s.add_data(4)
s.add_data(5)
s.add_data(3)
s.add_data(1)
s.print_list()
s.Search_and_print(5)