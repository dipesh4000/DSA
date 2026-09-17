# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        if not root:
            return []

        ans = []

        def dfs(path, node):
            if not node:
                return
            if path == "":
                path += str(node.val)
            else:
                path = path + "->" + str(node.val)
            if not node.left and not node.right:
                ans.append(path)
            else:
                dfs(path, node.left)
                dfs(path, node.right)

        dfs("", root)
        return ans
