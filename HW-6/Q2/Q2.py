class Queue:
    inner_list = []
    top = 0
    
    def enqueue(self, value):
        self.inner_list.insert(self.top, value)
        self.top = self.top + 1

    def dequeue(self):
        value = self.inner_list.pop(0)
        return value
    
    def delete(self, data):
        size = len(self.inner_list)
        for i in range(size):
            item = self.dequeue()
            if (data != item):
                self.enqueue(item)
        return self       
    
obj = Queue()
obj.enqueue(5)
obj.enqueue(7)
obj.enqueue(13)
obj.enqueue(4)
obj.enqueue(7)

obj.delete(7)
print(obj.dequeue())
print(obj.dequeue())
print(obj.dequeue())