# TC = O(1)
# SC = O(1)

class Solution:
    def intToRoman(self, num: int) -> str:
    # I avoided using a dictionary since it's unordered before Python 3.6, and I need to process numbers from largest to smallest in symList.

        sym_list = [["M", 1000], ["CM", 900], ["D", 500], ["CD", 400], ["C", 100], ["XC", 90], ["L", 50], ["XL", 40], ["X", 10], ["IX", 9], ["V", 5], ["IV", 4], ["I", 1]]

        integer = ""

        if num == "":
            return num

        for sym, val in sym_list: 
            count = num // val

            if count: 
                integer += (count * sym)
                num = num % val

            if num == 0:
                return integer


