class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n=len(bottomLeft)
        max_sarea=0
        for i in range(n-1):
            ax1,ay1=bottomLeft[i]
            ax2,ay2=topRight[i]
            for j in range(i+1,n):
                bx1,by1=bottomLeft[j]
                bx2,by2=topRight[j]
                if  not (ax2<=bx1 or ax1>=bx2 or ay1>=by2 or by1>=ay2):
                    width=max((min(ax2,bx2)-max(ax1,bx1)),0)
                    height=max((min(ay2,by2)-max(ay1,by1)),0)
                    if width*height>0:
                        max_sarea=max(max_sarea,min(width,height)**2)
        return max_sarea


        