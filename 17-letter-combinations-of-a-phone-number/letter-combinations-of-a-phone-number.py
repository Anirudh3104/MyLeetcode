class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_keypad = {"2": ["a", "b", "c"],
                        "3": ["d", "e", "f"],
                        "4": ["g", "h", "i"],
                        "5": ["j", "k", "l"],
                        "6": ["m", "n", "o"],
                        "7": ["p", "q", "r", "s"],
                        "8": ["t", "u", "v"],
                        "9": ["w", "x", "y", "z"]}
        res=[]
        def solve(index,curr,res):
            if index == len(digits):
                res.append(curr)
                return 
            for j in phone_keypad[digits[index]]:
                solve(index+1,curr+j,res)
        
        for j in phone_keypad[digits[0]]:
            solve(1,j,res)
        return res

       

        