class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import heapq
        product=1
        max_heap=[-x for x in nums]
        heapq.heapify(max_heap)
        heapq.heapify(nums)
        max1=-heapq.heappop(max_heap)
        max2=-heapq.heappop(max_heap)
        max3=-heapq.heappop(max_heap)
        min1=heapq.heappop(nums)
        min2=heapq.heappop(nums)
        product=max(max1*max2*max3,min1*min2*max1)
        return product

        