class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row,col=len(grid),len(grid[0])
        fresh=0
        queue=deque()
        for r in range(row):
            for c in range(col):
                if grid[r][c]==2:
                    queue.append((r,c))
                if grid[r][c]==1:
                    fresh+=1
        if not fresh: return 0
        time=-1
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        while queue:
            time+=1
            for _ in range(len(queue)):
                nx,ny=queue.popleft()
                for i,j in directions:
                    x,y=nx+i,ny+j 
                    if 0<=x<row and 0<=y<col and grid[x][y]==1:
                        queue.append((x,y))
                        grid[x][y]=2
                        fresh-=1

        return time if fresh==0 else -1
                             