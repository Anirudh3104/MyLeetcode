class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """n=len(nums)
        ex_sum=(n*(n+1))//2
        ac_sum=sum(nums)
        return ex_sum-ac_sum"""
        n=len(nums)
        i=0
        while i<n:
            crt_idx=nums[i]
            if nums[i]<n and nums[i]!=i:
                nums[i],nums[crt_idx]=nums[crt_idx],nums[i]
            else:
                i+=1
        for i in range(n):
            if i!=nums[i]:
                return i
        return n

        