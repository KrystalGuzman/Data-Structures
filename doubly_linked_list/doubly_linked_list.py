"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def __str__(self):

        output = []
        current_node = self.head
        
        while current_node:
            output.append(f"{current_node.prev} <- {current_node.value} -> {current_node.next}")
            current_node = current_node.next
        
        return "\n" + "\n".join(output) + "\n"

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        new_head = ListNode(value)
        self.length += 1
        #current DLL is empty
        if not self.head and not self.tail:
            #set new nodes next pointer to old head
            self.head = new_head
            self.tail = new_head
        else:
            #points new node to existing head
            new_head.next = self.head
            self.head.prev = new_head
            self.head = new_head

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        # prevent trying to remove from an empty DLL
        # if not self.head:
        #     return None
        # elif self.length == 1:
        #     return_value = self.head.value
        #     self.head = None
        #     self.tail = None
        #     self.length -= 1
        #     return return_value
        # else:
        #     removed_value = self.head
        #     self.head = self.head.next
        #     self.prev = None
        #     self.length -= 1
        #     return removed_value
        value = self.head.value
        self.delete(self.head)
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_tail = ListNode(value)
        self.length += 1
        #current DLL is empty
        if not self.tail and not self.head:
            #set new nodes next pointer to old tail
            self.head = new_tail
            self.tail = new_tail
        else:
            # #find current tail
            # current_tail = self.head
            # while current_tail.next:
            #     current_tail = current_tail.next
            # #points to new ListNode
            # current_tail.next = new_tail
            # #reassigns prev pointer of old tail
            # current_tail.next.prev = current_tail
            # #reassigns pointer to new tail
            # self.tail = current_tail.next

            new_tail.prev = self.tail
            self.tail.next = new_tail
            self.tail = new_tail


    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        #trying to remove from empty
        # if not self.head or not self.tail:
        #     return
        # elif self.length == 1:
        #     return_value = self.head.value
        #     self.head = None
        #     self.tail = None
        #     self.length -= 1
        #     return return_value
        # else:
        #     # store current tail
        #     removed_value = self.tail
        #     # move current tail pointer
        #     self.tail = self.tail.prev
        #     # set second elem's pre pointer to None
        #     self.tail.next = None
        #     #decrease length by 1
        #     self.length -= 1
        #     return removed_value
        value = self.tail.value
        self.delete(self.tail)
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        # do nothing if there is only one element in the list or node is already the head
        if self.length == 1 or node is self.head:
            return
        # delete and rewire prev and next pointers
        node.delete()
        # if this node happened to be the tail, move to the previous element
        if not node.next:
        #if node.next is None:
           self.tail = node.prev
        # update head pointer
        self.head.prev = node
        # reassign as head of list
        node.next = self.head
        node.prev = None
        # update head pointer
        self.head = node

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        # do nothing if only one element in list or node already at tail
        if self.length == 1 or node is self.tail:
            return
        # deletes and changes prev and next pointers
        node.delete()
        # if node is head, move to next element
        if not node.prev:
        #if node is self.head:
            self.head = node.next
        #  update tail pointer to point to new element
        self.tail.next = node
        # reassign as new tail
        node.prev = self.tail
        node.next = None
        #update tail pointer
        self.tail = node

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        #checks if head
        if node is self.head:
            current_next = self.head.next
            self.head = current_next
            #checks if tail
        if node is self.tail:
            current_prev = self.tail.prev
            self.tail = current_prev
        
        node.delete()
        self.length -= 1
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        current_node = self.head
        current_max = self.head.value
        
        while current_node.next:
            current_node = current_node.next
            #compares value and replaces if greater
            if current_node.value > current_max:
                current_max = current_node.value

        return current_max