class LRUCache:
    class node:
        def __init__(self,key,prev = None,next = None):
            self.key = key
            self.prev = prev
            self.next = next


    def __init__(self, capacity: int):
        self.linkMap = {}
        self.LRU = {}
        self.cap = capacity
        self.head = None
        self.tail = None


    def get(self, key: int) -> int:
        if key not in self.LRU:
            return -1
        
        existingNode = self.linkMap[key]
            
        if self.head is existingNode:
            pass 
        elif self.tail is existingNode:
            # dont needa check prev not being none in that case head was this and the first if passed in
            self.tail = existingNode.prev
            existingNode.prev.next = None
            existingNode.next = self.head
            existingNode.prev = None
            self.head.prev = existingNode
            self.head = existingNode
        else:
            existingNode.prev.next = existingNode.next
            existingNode.next.prev = existingNode.prev
            existingNode.prev = None
            existingNode.next = self.head
            self.head.prev = existingNode
            self.head = existingNode
        
        return self.LRU[key]

        

        

    def put(self, key: int, value: int) -> None:
        
        # already exists: updating
        if key in self.LRU:
            self.LRU[key] = value
            existingNode = self.linkMap[key]
            
            if self.head is existingNode:
                pass 
            elif self.tail is existingNode:
                # dont needa check prev not being none in that case head was this and the first if passed in
                self.tail = existingNode.prev
                existingNode.prev.next = None
                existingNode.next = self.head
                existingNode.prev = None
                self.head.prev = existingNode
                self.head = existingNode
            else:
                existingNode.prev.next = existingNode.next
                existingNode.next.prev = existingNode.prev
                existingNode.prev = None
                existingNode.next = self.head
                self.head.prev = existingNode
                self.head = existingNode
        
        # theres space: adding
        elif key not in self.LRU and len(self.LRU)<self.cap:
            
            self.LRU[key] = value
            newNode = self.node(key)
            self.linkMap[key] = newNode

            newNode.next = self.head
            if self.head:
                self.head.prev = newNode
            self.head = newNode

            # in the case of an empty list tail is at none
            if not self.tail:
                self.tail = newNode
        

        # out of sapce: evicting + adding
        elif len(self.LRU) == self.cap:
            toDel = self.tail.key
            del self.linkMap[toDel]
            del self.LRU[toDel]

            # evict:

            # edge case: length is 1
            if self.head is self.tail:
                self.head = None
                self.tail = None
            else:
                self.tail.prev.next = None
                self.tail = self.tail.prev

            
            # add:
            self.LRU[key] = value
            newNode = self.node(key)
            self.linkMap[key] = newNode

            newNode.next = self.head
            if self.head:
                self.head.prev = newNode
            self.head = newNode

            # in the case of an empty list tail is at none
            if not self.tail:
                self.tail = newNode   
