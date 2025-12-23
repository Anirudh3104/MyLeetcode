class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row=len(board)
        col=len(board[0])
        vis=[[0 for i in range(col)]for j in range(row)]
        queue=deque()
        for i in range(row):
            for j in  range(col):
                if i==0 or i==row-1 or j==0 or j==col-1:
                    if board[i][j]=='O':
                        vis[i][j]=1
                        queue.append((i,j))
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        while queue:
            for _ in range(len(queue)):
                r,c=queue.popleft()
                for i,j in directions:
                    nr,nc=r+i,c+j
                    if 0<=nr<row and 0<=nc<col and not vis[nr][nc]:
                        if board[nr][nc]=='O':
                            vis[nr][nc]=1
                            queue.append((nr,nc))
        for i in range(row):
            for j in range(col):
                if board[i][j]=='O' and not vis[i][j]:
                    board[i][j]='X'
        


                        



                    
        