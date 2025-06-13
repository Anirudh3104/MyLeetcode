class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        summ=nums[0]
        for i in range(len(nums)-1):
            if nums[i+1]==nums[i]+1:
                summ+=nums[i+1]
            else:
                break
        num_set=set(nums)
        while summ in nums:
            summ+=1
        return summ
            
        