class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        rec1Area=(ax2-ax1)*(ay2-ay1)
        rec2Area=(bx2-bx1)*(by2-by1)
        w_overlap=min(ax2,bx2)-max(ax1,bx1)
        h_overlap=min(ay2,by2)-max(ay1,by1)
        if w_overlap>0 and h_overlap>0:
            overlap=w_overlap*h_overlap
            return rec1Area+rec2Area-overlap
        return rec1Area+rec2Area
        