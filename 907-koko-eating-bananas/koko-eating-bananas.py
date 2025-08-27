class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def ispossible(k):
            hours=0
            for bananas in piles:
                hours+=ceil(bananas/k)
            return hours
        low=1
        high=max(piles)
        while high>=low:
            k=(low+high)//2
            hours=ispossible(k)
            if hours<=h:
                high=k-1
            else:
                low=k+1
        return low



            
            
            
            

        