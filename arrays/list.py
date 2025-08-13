class List:
    _arr = []
    _len = 0
    _capacity = 5

    def __init__(self):
        self._capacity = 5
        self._arr = [None] * self._capacity
        self._len = 0
    
    def get(self, index: int) -> int:
        if index < 0 or index >= self._len:
            raise IndexError(f"Index {index} is out of bounds 0 - {self._len}")
        
        return self._arr[index]

    def _check_and_grow(self):
        if self._len < self._capacity:
            return
        
        self._capacity *= 2

        arr = [None] * self._capacity

        for i in range(0, self._len):
            arr[i] = self._arr[i]

        self._arr = arr

    def insert_at(self, index: int, value: int):
        self._check_and_grow()

        if index < 0 or index > self._len:
            raise IndexError(f"Index {index} out of bounds 0 - {self._len}")

        if index != self._len:        
            for i in range(self._len - 1, index - 1, -1):
                self._arr[i + 1] = self._arr[i]

        self._arr[index] = value

        self._len += 1
    
    def remove_at(self, index: int) -> int:
        if index < 0 or index >= self._len:
            raise IndexError(f"Index {index} out of bounds 0 - {self._len}")
        
        v = self._arr[index]

        for i in range(index, self._len):
            self._arr[i] = self._arr[i + 1]
        
        self._arr[self._len - 1] = None

        self._len -= 1

        return v

    def __len__(self):
        return self._len