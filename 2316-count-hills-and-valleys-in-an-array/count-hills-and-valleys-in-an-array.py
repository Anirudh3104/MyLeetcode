class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        n=len(nums)
        ans=0
        for i in range(1,n-1):
            if nums[i]==nums[i-1]:
                continue
            left=None
            for j in range(i-1,-1,-1):
                if nums[j]!=nums[i]:
                    left=nums[j]
                    break
            right=None
            for z in range(i+1,n):
                if nums[z]!=nums[i]:
                    right=nums[z]
                    break
            if left and right and  left<nums[i]>right :
                ans+=1
            elif left and right and left>nums[i]<right:
                ans+=1
            else:continue
        return ans