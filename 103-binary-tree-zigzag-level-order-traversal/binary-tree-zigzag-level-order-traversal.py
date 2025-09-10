# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        arr=[]
        queue=deque([root])
        left_to_right=True
        while queue:
            levels=[]
            for _ in range(len(queue)):
                node=queue.popleft()
                levels.append(node.val)
                if node.left:queue.append(node.left)
                if node.right:queue.append(node.right)
            if not left_to_right:
                levels=levels[::-1]
            left_to_right=not left_to_right
            arr.append(levels)
        return arr


        