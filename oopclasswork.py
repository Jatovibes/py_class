class Mylist:
    def __init__(self, data):
        self.data = data

    def get_item(self, index):
        return self.data[index]
    
    def get_slice(self,start,end):
        return self.data[start:end]
    
list = Mylist([1,2,3,4,5])
print(list.get_item(2))
new_list = list.get_slice(1,4)
print(list.data)