class TreeNode(object):
    def __init__(object):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
