"""HashMap core realisation"""

from typing import Any


class HashMap:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.buckets = [[] for _ in range(self.capacity)]

    def put(self, key: str, value: Any):
        index = hash(key) % self.capacity

        bucket = self.buckets[index]

        for i, (stored_key, _) in enumerate(bucket):
            if stored_key == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))

    def get(self, key: str) -> Any:
        index = hash(key) % self.capacity

        bucket = self.buckets[index]

        for stored_key, value in bucket:
            if stored_key == key:
                return value

        raise KeyError(key)

    def delete(self, key: str):
        index = hash(key) % self.capacity
        
        bucket = self.buckets[index]

        for i, (stored_key, _) in enumerate(bucket):
            if stored_key == key:
                bucket.pop(i)
                return

        raise KeyError(key)
