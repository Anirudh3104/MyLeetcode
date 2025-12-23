class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        vis=[[0 for i in range(col)]for j in range(row)]
        queue=deque()
        for i in range(row):
            for j in range(col):
                if i==0 or i==row-1 or j==0 or j==col-1:
                    if grid[i][j]:
                        queue.append((i,j))
                        vis[i][j]=1
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        while queue:
            r,c=queue.popleft()
            for i,j in directions:
                nr,nc=i+r,j+c
                if 0<=nr<row and 0<=nc<col and grid[nr][nc] and not vis[nr][nc]:
                    vis[nr][nc]=1
                    queue.append((nr,nc))
        count=0
        for i in range(row):
            for j in range(col):
                if (not vis[i][j]) and grid[i][j]:
                    count+=1
        return count   

        