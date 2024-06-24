# https://www.youtube.com/watch?v=nBe_Ych7XUY

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        res = []

        phone_map = {
           "0": "", 
           "1": "",
           "2": "abc", 
           "3": "def",
           "4": "ghi", 
           "5": "jkl", 
           "6": "mno", 
           "7": "pqrs", 
           "8": "tuv", 
           "9": "wxyz"  
        }


        def backtrack(combination, next_digits):
            if len(next_digits) == 0:
                res.append(combination)
                return

            for letter in phone_map[next_digits[0]]:
                backtrack(combination + letter, next_digits[1:])

        res = []
        backtrack("", digits)
        return res


        