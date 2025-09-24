class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[-1]*n
        dp[-1]=0
        for i in range(n-2,-1,-1):
            farthest=min(n-1,i+nums[i])
            minn=float('inf')
            for j in range(i+1,farthest+1):
                minn=min(minn,dp[j])
            dp[i]=minn+1
        return dp[0]
        