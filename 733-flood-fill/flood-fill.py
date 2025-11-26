class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc]==color:return image
        row,col=len(image),len(image[0])
        queue=deque()
        queue.append((sr,sc))
        prev_color=image[sr][sc]
        image[sr][sc]=color
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        while queue:
            for _ in range(len(queue)):
                r,c=queue.popleft()
                for i,j in directions:
                    nr,nc=r+i,c+j
                    if 0<=nr<row and 0<=nc<col and image[nr][nc]!=color and image[nr][nc]==prev_color:
                        queue.append((nr,nc)) 
                        image[nr][nc]=color
        return image


        