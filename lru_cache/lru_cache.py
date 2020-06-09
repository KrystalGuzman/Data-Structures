from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.cache = DoublyLinkedList()
        self.storage = dict()
        self.limit = limit


    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):

        # key not in dictionary
        if key not in self.storage:
            return None
        
        # move value to end of list
        # return the requested value
        else:
            existing = self.storage[key]
            self.cache.move_to_end(existing)
            return existing.value[key]

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):

        # if the key exists in the cache, update the old entry
        if key in self.storage:

            # update existing value in existing
            existing = self.storage[key]
            data = dict()
            data[key] = value
            existing.value = data
            
            # point to the updated, most-recent-used value
            self.cache.move_to_end(existing)

        # key doesn't exist in the cache yet
        else:

            # if the cache is full, remove the least recent used value from the cache
            # also remove the key from the dictionary
            if len(self.cache) == self.limit:

                data_remove = self.cache.remove_from_head().value
                key_remove = [*data_remove][0]
                
                del self.storage[key_remove]

            # add to the most-recent-used spot (tail end)
            # add value to cache. Change to most recently used value
            data = dict()
            data[key] = value
            self.cache.add_to_tail(data)

            # add the new key to the dictionary.
            self.storage[key] = self.cache.tail