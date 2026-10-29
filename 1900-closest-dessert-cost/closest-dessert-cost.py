class Solution:
    def closestCost(self, baseCosts: list[int], toppingCosts: list[int], target: int) -> int:
        best = float("inf")
        def solve(toppings,index,currcost,target):
            nonlocal best
            if abs(currcost -target) < abs(best - target): ##choose the least diff(closest) cost to the target
                best = currcost
            elif abs(currcost-target) == abs(best-target): ##choose the min cost at equal diffs
                best = min(best,currcost)
            if currcost>=target: ##if the current is already = or > target choosing toppings aint gonna reduce the diff
                return
            if index == len(toppings): ##if we are out of the toppings array return to daddy call
                return
            
            solve(toppings,index+1,currcost,target) ##choosing 0 topping of the current choice and going forward
            solve(toppings,index+1,currcost+toppings[index],target) ##choosing one of the current topping and moving forward
            solve(toppings,index+1,currcost+2*toppings[index],target) ##choosing 2 of the current topping and moving forward
        for i in range(len(baseCosts)):
            solve(toppingCosts,0,baseCosts[i],target)
        return best 