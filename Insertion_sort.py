class Sorting:
    def __init__(self):
        self.list = []
    
    def add_data(self, data):
        # If the list is empty, simply add the data
        if not self.list:
            self.list.append(data)
        else:
            # Insert data in the correct position to keep the list sorted
            inserted = False
            for i in range(len(self.list)):
                if data < self.list[i]:
                    self.list.insert(i, data)
                    inserted = True
                    break
            if not inserted:
                # If data is larger than all elements, append it to the end
                self.list.append(data)
    
    def print_list(self):
        print("list =", self.list)

# Example usage
s = Sorting()
s.add_data(4)
s.add_data(5)
s.add_data(3)
s.add_data(1)
s.print_list()
