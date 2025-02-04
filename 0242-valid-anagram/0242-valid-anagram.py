# 1st Approach: sort both the string lexicographically by using sorted function and compare the sorted string. if both sorted string are same then return True else False

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return ''.join(sorted(s)) == ''.join(sorted(t))