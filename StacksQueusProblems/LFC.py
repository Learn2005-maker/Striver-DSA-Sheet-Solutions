class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1

        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):

        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = 0

    # Add node at front
    def add(self, node):

        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

        self.size += 1

    # Remove node
    def remove(self, node):

        node.prev.next = node.next
        node.next.prev = node.prev

        self.size -= 1

    # Remove least recently used node
    def remove_last(self):

        if self.size == 0:
            return None

        node = self.tail.prev

        self.remove(node)

        return node


class LFUCache:

    def __init__(self, capacity):

        self.capacity = capacity
        self.size = 0

        # key -> Node
        self.cache = {}

        # frequency -> DLL
        self.freq_map = {}

        # Minimum frequency
        self.min_freq = 0

    # Increase frequency of a node
    def update_frequency(self, node):

        old_freq = node.freq

        # Remove from old frequency list
        old_list = self.freq_map[old_freq]
        old_list.remove(node)

        # If old list becomes empty
        if old_freq == self.min_freq and old_list.size == 0:
            self.min_freq += 1

        # Increase frequency
        node.freq += 1

        new_freq = node.freq

        # Create DLL if frequency doesn't exist
        if new_freq not in self.freq_map:
            self.freq_map[new_freq] = DoublyLinkedList()

        # Add node to new frequency list
        self.freq_map[new_freq].add(node)

    def get(self, key):

        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Node was used, increase frequency
        self.update_frequency(node)

        return node.value

    def put(self, key, value):

        if self.capacity == 0:
            return

        # Key already exists
        if key in self.cache:

            node = self.cache[key]

            node.value = value

            # Updating value counts as using the key
            self.update_frequency(node)

            return

        # Cache is full
        if self.size == self.capacity:

            # Get lowest frequency list
            freq_list = self.freq_map[self.min_freq]

            # Remove LRU node from that frequency
            lru_node = freq_list.remove_last()

            # Remove from HashMap
            del self.cache[lru_node.key]

            self.size -= 1

        # Create new node
        node = Node(key, value)

        # New node always has frequency 1
        self.cache[key] = node

        # Create frequency 1 list if needed
        if 1 not in self.freq_map:
            self.freq_map[1] = DoublyLinkedList()

        self.freq_map[1].add(node)

        # New minimum frequency is 1
        self.min_freq = 1
        self.size +=1


lfu=LFUCache(3)
lfu.put(9,10)
lfu.put(4,5)

print(lfu.get(4))
lfu.put(4,100)
# print()





# Time complexcity:O(1) and s.c : O (capacity)



# ┌─────────────────────────────────────────────┐
# │                 LFU CACHE               │
# │                                         │
# │  cache                                  │
# │  ─────                                  │
# │  key ─────────────→ Node                `│
# │                     │                   │
# │                     │ freq              │
# │                     ↓                   │
# │              freq_map[freq]             │
# │                     │                   │
# │                     ↓                   │
# │              Doubly Linked List         │
# │                                         │
# │ min_freq ─────→ tells which DLL to check`│
# └─────────────────────────────────────────────┘

