"""Binary Search Tree core realisation"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, root, value):
        if root is None:
            return TreeNode(value)

        if value < root.val:
            root.left = self._insert(root.left, value)
        else:
            root.right = self._insert(root.right, value)

        return root

    def search(self, value):
        current = self.root

        while current:
            if current.val == value:
                return True

            if value < current.val:
                current = current.left
            else:
                current = current.right

        return False

    def find_min(self):
        if self.root is None:
            return None

        current = self.root

        while current.left:
            current = current.left

        return current.val

    def find_max(self):
        if self.root is None:
            return None

        current = self.root

        while current.right:
            current = current.right

        return current.val