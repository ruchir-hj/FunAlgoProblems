class TreeNode(object):
    def __init__(self, x):
        self.val = val
        self.left = left
        self.right = right

# solution 1 (DFS, recursive)
# Time O(n)
# Space O(h)
class Solution(object):
    def inverTree(self, root):
        if root is not None:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

# solution 2 (stack)
# Time O(n)
# Space O(h)
class Solution2:
     def invertTree(Self, root):
         nodes = []
         nodes.append(root)
         while nodes:
             node = nodes.pop()
             node.left, node.right = node.right, node.left
             if node.left is not None:
                 nodes.append(node.left)
             if node.right is not None:
                 nodes.append(node.right)       
