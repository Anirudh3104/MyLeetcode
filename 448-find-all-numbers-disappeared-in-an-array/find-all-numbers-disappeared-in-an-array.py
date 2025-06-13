class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # n=len(nums)
        # i=0
        # res=[]
        # while i<n:
        #     crt_idx=nums[i]-1
        #     if nums[i]!=nums[crt_idx]:
        #         nums[i],nums[crt_idx]=nums[crt_idx],nums[i]
        #     else:
        #         i+=1
        # for i in range(n):
        #     if nums[i]!=i+1:
        #         res.append(i+1)
        # return res
        for num in nums:
            idx=abs(num)-1
            nums[idx]=-abs(nums[idx])
        return [i+1 for i in range(len(nums)) if  nums[i]>0]
        