class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums=[i for i in range(1,10)]
        length=len(nums)
        sol=[]
        def backtrack(start,total,comb):
            if len(comb)==k and total==n:
                sol.append(comb[:])
                return 
            for i in range(start,length):
                if len(comb)>k or total>n:
                    break
                comb.append(nums[i])
                backtrack(i+1,total+nums[i],comb)
                comb.pop()
                
        backtrack(0,0,[])
        return sol