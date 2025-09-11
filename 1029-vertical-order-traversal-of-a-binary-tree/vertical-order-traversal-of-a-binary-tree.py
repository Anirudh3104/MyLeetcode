# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:return []
        arr=[]
        d={}
        queue=deque([(root,0,0)])
        while queue:
            for _ in range(len(queue)):
                node,row,col=queue.popleft()
                if col not in d:
                    d[col]={}
                if row not in d[col]:
                    d[col][row]=[]
                d[col][row].append(node.val)
                if node.left:queue.append((node.left,row+1,col-1))
                if node.right:queue.append((node.right,row+1,col+1))
        for col in sorted(d.keys()):
            a=[]
            for row in sorted(d[col].keys()):
                a.extend(sorted(d[col][row]))
            arr.append(a)
        return arr


