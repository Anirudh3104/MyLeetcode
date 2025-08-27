class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k>len(bloomDay):
            return -1
        def ispossible(x):
            flowers=0
            bouquets=0
            for days in bloomDay:
                if days<=x:
                    flowers+=1
                    if flowers==k:
                        bouquets+=1
                        flowers=0
                else:
                    flowers=0
            return bouquets>=m
        low,high=1,max(bloomDay)
        while high>=low:
            x=(low+high)//2
            if ispossible(x):
                high=x-1
            else:low=x+1
        return low
            

        