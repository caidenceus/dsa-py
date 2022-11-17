class IntHashNode(object):
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next
    
    def __repr__(self):
        return f'<IntHashNode object [{self.key}: {self.value}] -> {self.next}>'

    def __str__(self):
        return f'[{self.key}: {self.value}] -> {self.next}'


class IntHashTable(object):
    def __init__(self, size):
        self._table = [None] * size
        self._size = size
    
    def __str__(self):
        rtn = '['
        for value in self._table:
            rtn += str(value)
            rtn += ', '
        rtn = rtn[:-2]  # Remove last ', ' added by for loop
        rtn += ']'
        return rtn
    
    def __getitem__(self, key):
        return self.get(key)
    
    def _hash(self, value):
        return value % self._size
    
    def insert(self, key, value):
        index = self._hash(key)
        new_node = IntHashNode(key, value, None)

        if not self._table[index]:
            self._table[index] = new_node
            return
        
        last = self._table[index]
        while last.next:
            last = last.next
        last.next = new_node
    
    def get(self, key):
        index = self._hash(key)
        list_head = self._table[index]
        
        if not list_head:
            return None
        
        while list_head:
            if list_head.key == key:
                return list_head.value
            list_head = list_head.next
        
        return None
    
    def remove(self, key):
        # Note: because we call self.get, remove takes O(2n) time worst case which simplifies to O(n) time
        if not self.get(key):
            return
        
        index = self._hash(key)
        head = self._table[index]

        # Remove head if it contains the key
        if head.key == key:
            self._table[index] = head.next
            return
        
        # We can assume head.next always exists because we asserted the key exists
        while head.next.key != key:
            head = head.next
        head.next = head.next.next
