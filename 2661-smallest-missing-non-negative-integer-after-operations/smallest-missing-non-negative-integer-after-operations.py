class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        mod={}
        for num in nums:
            x=num%value
            if x in mod:
                mod[x]+=1
            else:
                mod[x]=1
        i=0 
        while True:
            r=i%value
            if mod.get(r, 0) > 0:
                mod[r]-=1
                i+=1
            else:
                return i
                    
        