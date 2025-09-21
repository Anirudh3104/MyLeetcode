class Solution:
    import heapq
    def thirdMax(self, nums: List[int]) -> int:
        nums=list(set(nums))
        if len(nums)<3:
            return max(nums)
        # max_heap=[-x for x in nums]
        # heapq.heapify(max_heap)
        # for i in range(2):
        #     heapq.heappop(max_heap)
        # return -heapq.heappop(max_heap)
        a,b,c=nums[0],float("-inf"),float("-inf")
        for i in range(1,len(nums)):
            if nums[i]>a:
                c=b
                b=a
                a=nums[i]
            elif nums[i]>b:
                c=b
                b=nums[i]
            elif nums[i]>c:
                c=nums[i]
            else:pass
        return c

        