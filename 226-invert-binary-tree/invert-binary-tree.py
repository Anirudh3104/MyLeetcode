# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        def invert(node):
            if not node:return 
            if not node.right and not node.left:return 
            temp=node.left
            node.left=node.right
            node.right=temp
            invert(node.left)
            invert(node.right)
        invert(root)
        return root