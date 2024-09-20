class Sorting:
    def __init__(self):
        self.list = []

    def add_data(self, data):
        self.list.append(data)

    def print_list(self):
        print("list = ", self.list)

    def Binary_search(self, data, item):
        low = 0
        high = len(data) - 1
        while low <= high:
            mid_index = (low + high) // 2  
            if data[mid_index] == item:
                return mid_index  
            elif item < data[mid_index]:
                high = mid_index - 1  
            else:
                low = mid_index + 1  
        
        return -1

    def Search_and_print(self, item):
        self.list.sort()  
        print("Sorted list:", self.list)
        result = self.Binary_search(self.list, item)
        
        if result != -1:
            print(f"Item {item} found at index {result}")
        else:
            print(f"Item {item} not found in the list")


# Example usage:
s = Sorting()
s.add_data(4)
s.add_data(5)
s.add_data(3)
s.add_data(1)
s.add_data(7)
s.add_data(2)

s.print_list()
s.Search_and_print(1)
