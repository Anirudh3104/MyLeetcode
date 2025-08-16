class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        def findfirst(nums,target):
            low,high,ans=0,len(nums)-1,-1
            while high>=low:
                mid=(low+high)//2
                if nums[mid]==target:
                    ans=mid
                    high=mid-1
                elif nums[mid]<target:
                    low=mid+1
                else:
                    high=mid-1
            return ans
        def findlast(nums,target):
            low,high,ans=0,len(nums)-1,-1
            while low<=high:
                mid=(low+high)//2
                if nums[mid]==target:
                    ans=mid
                    low=mid+1
                elif nums[mid]<target:
                    low=mid+1
                else:
                    high=mid-1
            return ans
        return [findfirst(nums,target),findlast(nums,target)]
                

                  

        