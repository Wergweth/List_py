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
    def delete(self, value):
        if self.head is None:
            print("the list is empty")
            return
        if self.head.value == value:
            self.head = self.head.next
            print("deleted")
            return
        current = self.head
        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
                print("deleted")
                return
            current = current.next

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

ll = LinkedList()
ll.insert(111)
ll.insert(222)
ll.insert(333)
ll.display()
ll.reverse()
ll.display()