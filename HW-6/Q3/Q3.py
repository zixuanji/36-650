#In summary, we can use 
#if not expression to conditionally execute a block of statements only if the value is not empty or not False.


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


# Class to create a Linked List
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    # Print the linked list
    def print_list(self):
        if self.head == None: #None is used to define a null value
            raise ValueError("List is empty")

        current = self.head #start from head
        while current: #tranversing (do we have the current) true is any non-zero 
            #value. The loop iterates while the condition is true.
            print(current.data, end="  ")
            current = current.next #point to the next one/travel to the next one
        print("\n")

    # Insert a node in a linked list
    def insert(self, data):
        node = Node(data)
        current = self.head 
        if not current:
            self.head = node
        else:
            while (current.next):
                current = current.next
            current.next = node
    
    # Find length of Linked List
    def size(self):
        if self.head == None:
            return 0

        size = 0
        current = self.head
        while current:
            size += 1
            current = current.next

        return size
    
    # Sort the nodes in a linked list
    def sortList(self):
        if not self.head:
            return
        c = self.head
        while c:
            n = c.next
            while n:
                if c.data > n.data:
                    tmp = n.data
                    n.data = c.data
                    c.data = tmp
                n = n.next
            c = c.next
            
first_node = Node(11)
linked_list = LinkedList(first_node) ## creating a linked list can start with a empty list and insert later
linked_list.insert(3)
linked_list.insert(6)
linked_list.insert(9)
linked_list.insert(2)
linked_list.insert(3)
linked_list.insert(6)
linked_list.insert(9)
linked_list.insert(2)
print("The Linked List is:")
linked_list.print_list()

linked_list.sortList()
print("After sorting, the Linked List is:")
linked_list.print_list()