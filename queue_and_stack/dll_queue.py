import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

new_list = DoublyLinkedList()
print(len(new_list))

class Queue:
    def __init__(self):
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()
        self.size = len(self.storage)

    def enqueue(self, value):
        self.storage.add_to_tail(value)

    def dequeue(self):
        if len(self.storage) == 0:
            return 
        else:
            return self.storage.remove_from_head()

    def len(self):
        self.size = len(self.storage)
        return self.size

new_queue = Queue()
new_queue.enqueue(2)
new_queue.enqueue(4)
print(new_queue.dequeue())
print(new_queue.len())

