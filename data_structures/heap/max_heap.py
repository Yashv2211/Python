class BinaryHeap:
    """
    A max-heap implementation in Python.

    >>> binary_heap = BinaryHeap()
    >>> binary_heap.insert(6)
    >>> binary_heap.insert(10)
    >>> binary_heap.insert(15)
    >>> binary_heap.insert(12)
    >>> binary_heap.pop()
    15
    >>> binary_heap.pop()
    12
    >>> binary_heap.get_list
    [10, 6]
    >>> len(binary_heap)
    2
    >>> binary_heap.peek()
    10
    >>> binary_heap.pop()
    10
    >>> binary_heap.pop()
    6
    >>> binary_heap.pop()
    Traceback (most recent call last):
        ...
    ValueError: Cannot pop from an empty heap!
    >>> binary_heap.peek()
    Traceback (most recent call last):
        ...
    ValueError: Cannot peek into an empty heap!
    """

    def __init__(self):
        self.__heap = [0]  # Initial element 0 (unused), heap starts at index 1.
        self.__size = 0

    def __swap_up(self, i: int) -> None:
        """Swap the element up the heap to maintain the heap property."""
        while i // 2 > 0:
            if self.__heap[i] > self.__heap[i // 2]:
                # Swap with parent if current node is greater than parent
                self.__heap[i], self.__heap[i // 2] = self.__heap[i // 2], self.__heap[i]
            i //= 2

    def insert(self, value: int) -> None:
        """Insert a new element into the heap."""
        self.__heap.append(value)
        self.__size += 1
        self.__swap_up(self.__size)

    def __swap_down(self, i: int) -> None:
        """Swap the element down the heap to maintain the heap property."""
        while 2 * i <= self.__size:
            bigger_child = self.__get_bigger_child(i)
            if self.__heap[i] < self.__heap[bigger_child]:
                # Swap current node with the larger of its children
                self.__heap[i], self.__heap[bigger_child] = self.__heap[bigger_child], self.__heap[i]
            i = bigger_child

    def __get_bigger_child(self, i: int) -> int:
        """Helper function to get the index of the larger child."""
        if 2 * i + 1 > self.__size:
            return 2 * i  # No right child, return left child
        else:
            # Return the bigger of the two children
            if self.__heap[2 * i] > self.__heap[2 * i + 1]:
                return 2 * i
            else:
                return 2 * i + 1

    def pop(self) -> int:
        """Pop the root element (maximum) from the heap."""
        if self.__size == 0:
            raise ValueError("Cannot pop from an empty heap!")

        max_value = self.__heap[1]
        self.__heap[1] = self.__heap[self.__size]
        self.__size -= 1
        self.__heap.pop()
        if self.__size > 0:
            self.__swap_down(1)
        return max_value

    def peek(self) -> int:
        """Peek at the maximum element without popping it."""
        if self.__size == 0:
            raise ValueError("Cannot peek into an empty heap!")
        return self.__heap[1]

    @property
    def get_list(self):
        """Return the list of elements in the heap (excluding the first element)."""
        return self.__heap[1:]

    def __len__(self):
        """Return the number of elements in the heap."""
        return self.__size


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Example usage:
    binary_heap = BinaryHeap()
    binary_heap.insert(6)
    binary_heap.insert(10)
    binary_heap.insert(15)
    binary_heap.insert(12)

    # Pop root (max-value since it is a max heap)
    print(binary_heap.pop())  # 15
    print(binary_heap.pop())  # 12

    # Get the list and size after operations
    print(binary_heap.get_list)  # [10, 6]
    print(len(binary_heap))  # 2

    # Peek at the maximum element
    print(binary_heap.peek())  # 10

    # Pop remaining elements
    print(binary_heap.pop())  # 10
    print(binary_heap.pop())  # 6
