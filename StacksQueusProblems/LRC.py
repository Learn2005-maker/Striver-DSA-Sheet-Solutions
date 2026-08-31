class Node:
    def __init__(self, key, value):
        self.prev = None
        self.next = None
        self.key = key
        self.value = value

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.cacheMap = {}
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def remove(self, node):
        prevNode = node.prev
        afterNode = node.next
        prevNode.next = afterNode  
        afterNode.prev = prevNode

    def afterhead(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        # FIXED: Removed [key] from the check
        if key not in self.cacheMap: 
            return -1
        node = self.cacheMap[key]  
        self.remove(node)  
        self.afterhead(node) 
        return node.value

    def put(self, key, value):
        # if key already exists
        if key in self.cacheMap:
            node = self.cacheMap[key] # FIXED: Added self.
            node.value = value
            self.remove(node)
            self.afterhead(node)
            return
        
        newnode = Node(key, value)
        self.cacheMap[key] = newnode # FIXED: node -> newnode
        self.afterhead(newnode)

        if len(self.cacheMap) > self.capacity:
            # Least recently used node
            lru = self.tail.prev

            self.remove(lru)
            del self.cacheMap[lru.key]

# Testing the code
lru = LRUCache(5)

lru.put(1, 10)
lru.put(2, 40)
print(lru.get(1)) # Output: 10

lru.put(3, 30)

print(lru.get(2)) # Output: 40
print(lru.get(3)) # Output: 30