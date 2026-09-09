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

            i = smallest


def heapify(arr):
    parent = (len(arr) // 2) - 1

    def sift_down(arr, i):
        n = len(arr)
        
        while True:
            left = 2 * i + 1
            right = 2 * i + 2

            smallest = i

            if left < n and arr[left] < arr[smallest]:
                smallest = left

            if right < n and arr[right] < arr[smallest]:
                smallest = right

            if smallest == i:
                break

            arr[i], arr[smallest] = arr[smallest], arr[i] 

            i = smallest

        return arr

    for i in range(parent, -1, -1):
        arr = sift_down(arr, i)

    return arr



if __name__ == '__main__':
    heap = MinHeap()

    heap.push(5)
    heap.push(3)
    heap.push(8)
    heap.push(1)
    heap.push(4)

    print("Push:")
    print(heap.heap)
    
    print("\nPop:")
    print("Удалили:", heap.pop())
    print("Heap:", heap.heap)

    print("Удалили:", heap.pop())
    print("Heap:", heap.heap)

    arr = [5, 3, 8, 1, 4]

    print("\nHeapify:")
    print("До:", arr)

    heap_arr = heapify(arr)

    print("После:", heap_arr)

    arr = [10, 2, 7, 1, 9, 3, 6, 4, 8, 5]

    print("\nHeapify 2:")
    print("До:", arr)

    heap_arr = heapify(arr)

    print("После:", heap_arr)

    heap = MinHeap()

    for value in [10, 20, 5, 3, 7, 1, 15]:
        heap.push(value)
        print(f"После push({value}):", heap.heap)

    print("\nВсе элементы по возрастанию:")

    while heap.heap:
        print(heap.pop(), end=" ")

    print()

    print("\n--- Manual practice ---")

    arr1 = [10, 5, 7, 2, 3]
    print("arr1:", arr1)
    print("heapify:", heapify(arr1))

    arr2 = [9, 4, 7, 1, 2, 6, 5]
    print("arr2:", arr2)
    print("heapify:", heapify(arr2))

    arr3 = [20, 15, 10, 5, 8, 3, 7, 1]
    print("arr3:", arr3)
    print("heapify:", heapify(arr3))
