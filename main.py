class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next
        print("--end--")

    def insert(self, value):
        new = Node(value)
        if self.head is None:
            self.head = new
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new

ll = LinkedList()
ll.insert(111)
ll.insert(222)
ll.display()