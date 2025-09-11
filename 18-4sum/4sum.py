class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        ans=[]
        nums.sort()
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                lo,hi=j+1,n-1
                while lo<hi:
                    summ=nums[i]+nums[j]+nums[lo]+nums[hi]
                    if summ==target:
                        ans.append([nums[i],nums[j],nums[lo],nums[hi]])
                        hi-=1
                        lo+=1
                        while lo<hi and nums[lo]==nums[lo-1]:
                            lo+=1
                        while lo<hi and nums[hi]==nums[hi+1]:
                            hi-=1
                    elif summ>target:
                        hi-=1
                    else: 
                        lo+=1
        return ans            


        