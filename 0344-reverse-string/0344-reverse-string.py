#if "i" is the elment from first then "(n - i - 1)"" is the ith elment form the last.
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)

        for i in range(n // 2):
            s[i], s[n - i - 1] = s[n - i - 1], s[i]

        
        