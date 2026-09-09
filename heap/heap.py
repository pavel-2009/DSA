"""Min heap core realisation"""


class MinHeap:
    """Min heap class"""

    def __init__(self):
        self.heap = []

    def push(self, val):
        self.heap.append(val)
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            raise IndexError("Heap is empty")

        if len(self.heap) == 1:
            return self.heap.pop()

        minimum = self.heap[0]

        self.heap[0] = self.heap.pop()
        self._sift_down(0)

        return minimum

    def _sift_up(self, i):
        while i > 0:
            parent = (i - 1) // 2

            if self.heap[parent] <= self.heap[i]:
                break

            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]

            i = parent

    def _sift_down(self, i):
        n = len(self.heap)

        while True:
            left = 2 * i + 1
            right = 2 * i + 2

            smallest = i

            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left

            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == i:
                break

            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i] 
