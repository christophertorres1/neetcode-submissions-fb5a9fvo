# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderDFSArray(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        return self.inorderDFSArray(root.left) + [root.val] + self.inorderDFSArray(root.right)
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = self.inorderDFSArray(root)
        return arr[k - 1]