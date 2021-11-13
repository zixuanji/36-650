class Node:
    def __init__(self, data):
        self.too_big = None
        self.big = None
        self.small = None
        self.data = data
    
    def insert(self, data):
# Compare the new value with the parent node
      if self.data:
        if (data-self.data) >=10 :
            if self.too_big is None:
                self.too_big = Node(data)
            else:
                self.too_big.insert(data)
        elif (data-self.data) >= 0 and (data-self.data) < 10:
            if self.big is None:
                self.big = Node(data)
            else:
                self.big.insert(data)
        elif (data-self.data) < 0:
            if self.small is None:
                self.small = Node(data)
            else:
                self.small.insert(data)
        else:
            self.data = data
    # Print the tree
    def traversal(self):
        if self.small:
            self.small.traversal()
        print(self.data)
        if self.big:
            self.big.traversal()
        if self.too_big:
            self.too_big.traversal()
            
    def traversal_list(self, new_list):
        
        if self.small:
            self.small.traversal_list(new_list)
        new_list.append(self.data)
        if self.big:
            self.big.traversal_list(new_list)
        if self.too_big:
            self.too_big.traversal_list(new_list)
        
        return new_list
        
    def delete(self, data):
        
        l = self.traversal_list([])
        self.too_big = None
        self.big = None
        self.small = None
        
        # delete the item in the list
        n = []
        for i in range(len(l)):
            if (data != l[i]):
                n.append(l[i])
        #insert again
        for j in range(1, len(n)):
            self.insert(n[j])
        

root = Node(20)
root.insert(40)
root.insert(45)
root.insert(32)

print("Tree contents after insertion using the traversal():")
root.traversal()

root.delete(45)
print("Tree contents after deleting 45 using the traversal():")
root.traversal()