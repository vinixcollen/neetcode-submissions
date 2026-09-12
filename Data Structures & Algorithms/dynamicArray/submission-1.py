class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.arr = [0] * self.capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
    
        self.arr[self.length] = n
        self.length += 1

    def popback(self) -> int:
        if self.length > 0:
            # soft delete
            self.length -= 1
        return self.arr[self.length]

    def resize(self) -> None:
        self.capacity *= 2
        # make new copy of arr
        new_arr = [0] * self.capacity

        # copy the elements in arr to new_arr
        for i in range(self.length):
            new_arr[i] = self.arr[i]
        # reinstantiate the new as current arr so it can be reused instead of using new_arr
        self.arr = new_arr

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity