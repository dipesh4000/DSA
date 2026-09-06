# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # mxdepth = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        # if not root:
        #     return 0

        # def getdepth(node: Optional[TreeNode], depth):
        #     if not node:
        #         return
        #     self.mxdepth = max(self.mxdepth, depth)
        #     getdepth(node.left, depth + 1)
        #     getdepth(node.right, depth + 1)

        # getdepth(root, 1)
        # return self.mxdepth
