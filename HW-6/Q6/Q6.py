# question 6

class Node(object):
    def __init__(self, data):
        self.data = data
        self.previous = None

class ReversedLinkedList(object):
    def __init__(self, tail=None):
        self.tail = tail
    
    # Print the linked list
    def print_list(self):
        if self.tail == None: #None is used to define a null value
            raise ValueError("List is empty")

        prev = self.tail #start from tail
        while prev: #tranversing (do we have the current) true is any non-zero 
            #value. The loop iterates while the condition is true.
            print(prev.data, end="  ")
            prev = prev.previous #point to the next one/travel to the next one
        print("\n")
        
    # Insert a node in a linked list
    def insert(self, data):
        new_node = Node(data)
        prev = self.tail
        self.tail = new_node
        new_node.previous = prev
    
    # Check if tail node is to be deleted
    def check_tail_del(self, data):
        if not self.tail:
            return
        
        tmp = self.tail
        if self.tail.data == data: 
            print("Deleted node is " + str(self.tail.data))
            self.tail = tmp.previous
            return True
        return False
        
        
    # Delete a node in a linked list
    def delete(self, data):
        if not self.tail:
            return
        if self.check_tail_del(data)== True:
            return
        temp = self.tail
        
        while temp.previous:
            if temp.previous.data == data:
                print("Node deleted is " + str(temp.previous.data))
                temp.previous = temp.previous.previous
                return
        temp = temp.previous
        print("Node not found")
        return 
        
        
    def search(self, data):
        if not self.tail:
            return
        c = self.tail
        while c:
            if (data == c.data):
                return True
            else:
                c = c.previous
        return False
        
last_node = Node(11)
linked_list = ReversedLinkedList(last_node)
linked_list.insert(3)
linked_list.insert(6)
linked_list.insert(5)
print("The Linked List is (after insertion):")
linked_list.print_list()
linked_list.delete(6)
print("The Linked List is (after deleting 6):")
linked_list.print_list()
linked_list.delete(5)
print("The Linked List is (after deleting 5):")
linked_list.print_list()
print("Does 5 exist in the Linked List?")
print(linked_list.search(5))
print("Does 7 exist in the Linked List?")
print(linked_list.search(7))
print("Does 11 exist in the Linked List?")
print(linked_list.search(11))