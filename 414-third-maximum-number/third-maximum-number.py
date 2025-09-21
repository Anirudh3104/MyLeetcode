class Solution:
    import heapq
    def thirdMax(self, nums: List[int]) -> int:
        nums=set(nums)
        if len(nums)<3:
            return max(nums)
        max_heap=[-x for x in nums]
        heapq.heapify(max_heap)
        for i in range(2):
            heapq.heappop(max_heap)
        return -heapq.heappop(max_heap)

        