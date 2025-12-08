class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        row,col=len(isWater),len(isWater[0])
        vis=[[0]*col for _ in range(row)]
        q=deque()
        for r in range(row):
            for c in range(col):
                if isWater[r][c]:
                    vis[r][c]=1
                    isWater[r][c]=0
                    q.append((r,c))
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            for _ in range(len(q)):
                x,y=q.popleft()
                for i,j in directions:
                    nx,ny=x+i,y+j
                    if 0<=nx<row and 0<=ny<col and not vis[nx][ny]:
                        isWater[nx][ny]=isWater[x][y]+1
                        q.append((nx,ny))
                        vis[nx][ny]=1
        return isWater

            

        