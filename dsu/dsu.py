class DSU:

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if x != self.parent[x]:
            # Прталкиваем элемент к корню
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return False

        if self.rank[a] > self.rank[b]:
            self.parent[root_a] = root_b

        elif self.rank[a] < self.rank[b]:
            self.rank[root_b] = root_b

        else:
            self.parent[root_b] = root_a
            self.rank[root_a] += 1

        return True
