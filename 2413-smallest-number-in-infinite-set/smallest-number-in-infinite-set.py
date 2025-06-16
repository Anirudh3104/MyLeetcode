class SmallestInfiniteSet:
    def __init__(self):
        self.curr=1
        self.heap=[]
        self.sett=set()
    def popSmallest(self) -> int:
        if self.heap and self.heap[0]<self.curr:
            smallest=heapq.heappop(self.heap)
            self.sett.remove(smallest)
            return smallest
        else:
            smallest=self.curr
            self.curr+=1
            return smallest
    def addBack(self, num: int) -> None:
        if num not in self.sett and num<self.curr:
            self.sett.add(num)
            heapq.heappush(self.heap,num)
        else:
            return None

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)