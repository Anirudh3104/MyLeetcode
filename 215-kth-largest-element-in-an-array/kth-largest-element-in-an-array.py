class Solution(object):
    import heapq
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        min_heap=[]
        for x in nums:
            heapq.heappush(min_heap,x)
            if len(min_heap)>k:
                heapq.heappop(min_heap)
        return heapq.heappop(min_heap)

        