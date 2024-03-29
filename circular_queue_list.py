class Empty(Exception):
    pass

class Full(Exception):
    pass

class ArrayQueue:
    DEFAULT_CAPACITY = 5

    def __init__(self):
        self._data = [None] * self.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def deque(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data) #return the index
        self._size = self._size - 1
        return answer

    def is_queue_full(self):
        return self._size == len(self._data)

    def enqueue(self, e):
        if self.is_queue_full():
            raise Full("Queue is Full")
        else:
            avail = (self._front + self._size) % len(self._data) #where index of empty space is there
            self._data[avail] = e
            self._size = self._size + 1

    def print_queue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            current = self._front
            print("Queue elements: ", end="")
            for i in range(self._size):
                print(self._data[current], end=" ")  #printing the first element
                current = (current + 1) % len(self._data) #after the first elements gets printed
            print()

x=ArrayQueue()
x.enqueue(5)
x.enqueue(6)
x.enqueue(0)
x.enqueue(1)
x.enqueue(2)
x.print_queue()
x.deque()
x.deque()
x.deque()
x.print_queue()

# [1,2,3,4,5]
# [None,None,3,4,5]
# [6,None,3,4,5]
# [6,2,3,4,5]
# front=3
# [6,2,None,4,5]
# [6,2,None,None,5]
# [6,2,None,None,None]

