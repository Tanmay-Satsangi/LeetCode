# https://www.youtube.com/watch?v=2SVKgAakQsU
# think to solve this problem just like to convert one number system to another number system (Ex: Decimal Number system to Binary Number System)

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = []

        while (columnNumber):
            columnNumber -=1 
            rem = columnNumber % 26
            columnNumber = columnNumber // 26

            ans.append(chr(65 + rem))

        return ''.join(ans[::-1])
        
        