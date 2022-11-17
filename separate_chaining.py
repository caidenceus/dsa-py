class HashNode(object):
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next
    
    def __repr__(self):
        return f'<IntHashNode object [{self.key}: {self.value}] -> {self.next}>'

    def __str__(self):
        return f'[{self.key}: {self.value}] -> {self.next}'


class HashTable(object):
    def __init__(self, size=89):
        self._table = [None] * size
        
        # Table capacity and number of items in table respectively
        self._size = size
        self._num_items = 0
    
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
    
    def __len__(self):
        return self._num_items
    
    @property
    def load_factor(self):
        return self._num_items / self._size
    
    def _hash(self, key):
        """Hash an object and return the hash mod self._table_size.

        Args:
            key (hashable object): The key to hash.

        Returns:
            int: The index of self._table for the hashed data.
        """
        return hash(key) % self._size

    def _double_size(self):
        """Double the capacity of the hash table."""
        new_size = self._size * 2
        new_table = [None] * new_size

        for i in range(0, self._size):
            new_table[i] = self._table[i]

        self._table = new_table
        self._size = new_size
    
    def insert(self, key, value):
        """Insert a node into the hash table

        Args:
            key (hashable object): The key to be hashed to lookup the node associated with the key value pair.
            value (any): The data to be stored in the node being inserted.
        """
        self._num_items += 1
        index = self._hash(key)
        new_node = IntHashNode(key, value, None)

        # Double the hash table capacity if it is full
        if self.load_factor >= 1:
            self._double_size()

        if not self._table[index]:
            self._table[index] = new_node
            return
        
        last = self._table[index]
        while last.next:
            last = last.next
        last.next = new_node
    
    def get(self, key):
        """Lookup a value in the table associated with a key.

        Args:
            key (hashable object): The key of the value to retrieve from the table.

        Returns:
            any: The value associated with key, or None if no such key exists.
        """
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
        """Remove a node from the hash table.

        Args:
            key (hashable object): The key of the node to remove from the table.
        """
        # Note: because we call self.get, remove takes O(2n) time worst case which simplifies to O(n) time
        if not self.get(key):
            return

        self._num_items -= 1
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
