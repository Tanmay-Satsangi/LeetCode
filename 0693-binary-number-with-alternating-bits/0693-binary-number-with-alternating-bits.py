class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bin_n = bin(n)

        if "00" in bin_n or "11" in bin_n:
            return False
        return True

        