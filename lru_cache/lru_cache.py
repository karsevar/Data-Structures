from doubly_linked_list import DoublyLinkedList

# new_list = DoublyLinkedList()
# new_key = 'itemA'
# new_value = 'valueflea'
# print({new_key: new_value})
# new_list.add_to_head({new_key: new_value})
# print(new_list.head.value)

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit 

        # create the doubly linked list storage variable
        # that will keep track of node ordering 
        self.storage = DoublyLinkedList()
 
        # create the cache_dict dictionary that will increate 
        # key lookup within the doubly linked list.
        self.dict_cache = {}
    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # check if the key is within the dict_cache 
        # if within the dict_cache 
            # move the referenced node to the front of the double linked 
            # list 
            # modify the dict_cache[key] to have the appropriate node reference 
            # return dict_cache[key].value[key]

        if key not in self.dict_cache:
            return None
        
        referenced_node = self.storage.move_to_front(self.dict_cache[key])
        self.dict_cache[key] = referenced_node
        return self.dict_cache[key].value[key]

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
        # edge cases:
        # if key in self.dict_cache the key is already in dict_cache
            # modify the value within the node that has same key 
            # move the modified node to the front of the doubly linked list 

        # if len(self.storage) == self.limit the size of the storage 
            # first obtain the key of the tail element that we will 
            # need to delete 
            # second use the self.storage.remove_from_tail() method 
            # to remove the least used element in cache 
            # third delete the key from the dict_cache 
            # fourth add the new element to the dict_cach and the 
            # doubly linked list.
          
        # else you can just add the new value into the dict_cache 
        # and the self.storage.

        if key in self.dict_cache:
            self.dict_cache[key].value = {key: value}
            self.dict_cache[key] = self.storage.move_to_front(self.dict_cache[key])

        elif len(self.storage) == self.limit:
            tail_key = list(self.storage.tail.value.keys())
            print(tail_key)
            self.storage.remove_from_tail()
            del self.dict_cache[tail_key[0]]
            
            new_dict_node = self.storage.add_to_head({key: value})
            self.dict_cache[key] = new_dict_node

        else:
            new_dict_node = self.storage.add_to_head({key: value})
            self.dict_cache[key] = new_dict_node

cache_stuff = LRUCache(3)
cache_stuff.set('itemA', 'fleame')
cache_stuff.set('itemB', 'meflea')
cache_stuff.set('itemC', 'mefleatothemax')
cache_stuff.set('itemD', 'flyingman!!!')
cache_stuff.set('itemB', 'meflea2')
cache_stuff.set('itemC', 'tincup!!!')
print(cache_stuff.dict_cache['itemC'].value)
print(cache_stuff.storage.head.next.value)
print(cache_stuff.storage.tail.value)



