class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        count=0
        summ=0
        sett=set([i for i in banned if i<=n])
        for i in range(1,n+1):
            if i not in sett and summ+i<=maxSum:
                count+=1
                summ+=i
        return count

        