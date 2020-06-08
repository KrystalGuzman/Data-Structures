"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack? pop is built in vs adding and removing from tail
"""
from singly_linked_list import LinkedList

# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.storage.append(value)
#         self.size += 1

#     def pop(self):

#         if self.size > 0:
#             self.size -= 1
#             return self.storage.pop()

class StackFromLinkedList:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    # new items will be appended at head of existing list for easy access to the most recently added element
    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):

        if self.size > 0:
            self.size -= 1
            return self.storage.remove_tail()

class Stack(StackFromLinkedList):
    def __init__(self):
        super().__init__()
