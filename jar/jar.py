class Jar:
    def __init__(self, capacity=12):
        self._size = 0
        self._capacity = capacity
        if self.capacity < 0:
            raise ValueError("Invalid capacity")

    def __str__(self):
        return self._size*"🍪"

    def deposit(self, n):
        if self._size + n <= self._capacity:
            self._size+=n
        else:
            raise ValueError("Max capacity reached")

    def withdraw(self, n):
        if self._size - n < 0:
            raise ValueError("Not enough cookies to withdraw")
        else:
            self._size-=n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size