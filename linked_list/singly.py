class SinglyNode(object):
    def __init__(self, data, next=None):
        """Initialize a singly linked list node.

        Args:
            data (any): Data to be held by this node.
            next (SinglyNode, optional): Optionally initialize the next pointer
                to another node. Defaults to None.
        """
        self.data = data
        self.next = next


class Singly(object):
    def __init__(self):
        """Initialize a singly linked list."""
        self._head = None
        self._size = 0

    def __str__(self):
        """String representation of linked list.

        Returns:
            str: String representation of list where contents of linked list is
                cast to a list.
        """
        output = list()
        temp = self._head
        while temp:
            output.append(temp.data)
            temp = temp.next
        return str(output)

    def __iter__(self):
        """Make linked list act as an iterator."""
        self._iter_node = self._head
        return self

    def __next__(self):
        """Get the next value of the iterator."""
        if not self._iter_node:
            raise StopIteration
        data = self._iter_node.data
        self._iter_node = self._iter_node.next
        return data

    def __len__(self):
        """O(1) Get the size of the list."""
        return self._size

    def __getitem__(self, index):
        """O(n) Allow list to be accessible by indicies.
        
        Args:
            index (int): Index of list element to return.
        
        Raises:
            IndexError: If index is greater than the length of the list.
        """
        if index >= len(self):
            err = f'{index} is larger than list size: {len(self)}'
            raise IndexOutOfRange(err)

        current = self._head
        for i in range(index):
            current = current.next
        return current.data
    
    def __setitem__(self, index, data):
        """O(n) Allow list node data to be mutable by indicies.
        
        Args:
            index (int): Index of list item to set.
            data (any): Value to override the existing list data with.
        
        Raises:
            IndexError: If index is greater than the length of the list.
        """
        if index >= len(self):
            err = f'{index} is larger than list size: {len(self)}'
            raise IndexOutOfRange(err)

        current = self._head
        for i in range(index):
            current = current.next
        current.data = data

    def prepend(self, data):
        """Insert a node at the beginning of the list.

        Args:
            data (any): Data to be held by the new list head.
        """
        self._size += 1
        new_head = SinglyNode(data)
        new_head.next = self._head
        self._head = new_head

    def insert(self, data, index):
        """Insert a node into a linked list at an index; indexing starts at 0.

        Args:
            data (any): Data to insert into the list.
            index (int): Index of list to insert data; self._head has index 0.

        Raises:
            IndexError: If index > 0 and list is empty.
            IndexError: If index is greater than the length of the list.
        """
        err_msg = f'Index {index} is out of range.'

        if index == 0:
            self.prepend(data)
            return

        # Can only insert to head of an empty list
        if not self._head:
            raise IndexError(err_msg)

        # Find the node directly before where we wish to insert the new node
        temp = self._head
        while index - 1:
            index -= 1
            temp = temp.next
            if not temp:
                raise IndexError(err_msg)

        new_node = SinglyNode(data, temp.next)
        temp.next = new_node
        self._size += 1

    def append(self, data):
        """Add a node to the end of the list.

        Args:
            data (any): Data to be held by the new list head.
        """
        self._size += 1
        new_tail = SinglyNode(data)
        temp = self._head

        # If list is empty, update the head and return
        if not temp:
            self._head = new_tail
            return

        # Update temp to point to the current tail of the list
        while temp.next:
            temp = temp.next
        temp.next = new_tail

    def delete(self, index):
        """Delete a node of the list by index; indexing starts at 0.

        Args:
            index (int): Index of node to delete; self._head has index 0.

        Raises:
            IndexError: If index is greater than the length of the list.
        """
        if index == 0 and self._head:
            self._head = self._head.next
            self._size -= 1
            return

        temp = self._head
        while index - 1:
            index -= 1
            temp = temp.next
            if not temp:
                err_msg = f'Index {index} is out of range.'
                raise IndexError(err_msg)
        temp.next = temp.next.next
        self._size -= 1
