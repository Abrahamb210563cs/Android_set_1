class MyHashMap:
    def __init__(self):
        self.size = 1009  # A prime number to reduce collisions
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        for i, (k, v) in enumerate(self.buckets[index]):
            if k == key:
                self.buckets[index][i] = (key, value)  # Update
                return
        self.buckets[index].append((key, value))  # Insert

    def get(self, key: int) -> int:
        index = self._hash(key)
        for k, v in self.buckets[index]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        index = self._hash(key)
        self.buckets[index] = [(k, v) for k, v in self.buckets[index] if k != key]

