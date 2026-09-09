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


def heapify(arr):
    parent = (len(arr) // 2) - 1

    def sift_up(arr, i):
        while i > 0:
            parent = (i - 1) // 2

            if arr[parent] <= arr[i]:
                break

            arr[parent], arr[i] = arr[i], arr[parent]

            i = parent

        return arr

    for i in range(parent, 0, -1):
        arr = sift_up(arr, i)

    return arr



if __name__ == '__main__':
    heap = MinHeap()

    heap.push(5)
    heap.push(3)
    heap.push(8)
    heap.push(1)
    heap.push(4)

    print(heap.heap)


