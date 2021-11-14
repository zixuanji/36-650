# Question 5

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
    
    # remove duplicates
    def remove_dups(self):
        if not self.head:
            return
        c = self.head # start from head
        while c:
            n = c
            # Compare with the rest of the linked list
            while n.next:
                # delete duplicates
                if (c.data == n.next.data):
                    n.next = n.next.next
                else:
                    n = n.next
            c = c.next

first_node = Node(11)
linked_list = LinkedList(first_node)
linked_list.insert(3)
linked_list.insert(6)
linked_list.insert(5)
linked_list.insert(3)
linked_list.insert(11)
linked_list.insert(6)
linked_list.insert(5)
linked_list.insert(7)
linked_list.insert(5)
linked_list.insert(6)
print("The Linked List is:")
linked_list.print_list()

linked_list.remove_dups()
print("After removing the duplications, the Linked List is:")
linked_list.print_list()s