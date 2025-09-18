# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count=0
        def isgoodnode(node,maxval):
            nonlocal count
            if not node:return 
            if node.val>=maxval:
                count+=1
                maxval=node.val
            isgoodnode(node.left,maxval)
            isgoodnode(node.right,maxval)
        isgoodnode(root,root.val)
        return count
        