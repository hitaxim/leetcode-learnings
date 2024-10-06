class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k              # Size of the queue
        self.queue = [0] * k   # Initialize the queue with size k
        self.front = -1         # Front pointer
        self.rear = -1          # Rear pointer
        self.size = 0           # Current size of the queue

    def Front(self) -> int:
        """ Get the front item from the queue. """
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        """ Get the last item from the queue. """
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def enQueue(self, value: int) -> bool:
        """ Insert an element into the circular queue. """
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = 0  # Set front to 0 when queue is empty
        self.rear = (self.rear + 1) % self.k  # Move rear to next position
        self.queue[self.rear] = value          # Insert the value
        self.size += 1                          # Increase the size
        return True

    def deQueue(self) -> bool:
        """ Delete an element from the circular queue. """
        if self.isEmpty():
            return False
        if self.front == self.rear:  # Only one element was present
            self.front = -1           # Reset pointers
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.k  # Move front to next position
        self.size -= 1  # Decrease the size
        return True

    def isEmpty(self) -> bool:
        """ Check whether the circular queue is empty or not. """
        return self.size == 0

    def isFull(self) -> bool:
        """ Check whether the circular queue is full or not. """
        return self.size == self.k

# Example usage:
circularQueue = MyCircularQueue(3)  # Size of the queue is 3
print(circularQueue.enQueue(1))      # returns True
print(circularQueue.enQueue(2))      # returns True
print(circularQueue.enQueue(3))      # returns True
print(circularQueue.enQueue(4))      # returns False (queue is full)
print(circularQueue.Rear())           # returns 3
print(circularQueue.isFull())         # returns True
print(circularQueue.deQueue())        # returns True
print(circularQueue.enQueue(4))      # returns True
print(circularQueue.Rear())           # returns 4
