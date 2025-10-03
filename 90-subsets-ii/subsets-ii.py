class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res,sol=[],[]
        n=len(nums)
        def backtrack(sol,i):
            if i==n:
                if sol not in res:
                    res.append(sol.copy())
                return 
            sol.append(nums[i])
            backtrack(sol,i+1)

            sol.pop()
            backtrack(sol,i+1)
        backtrack(sol,0)
        return res


        