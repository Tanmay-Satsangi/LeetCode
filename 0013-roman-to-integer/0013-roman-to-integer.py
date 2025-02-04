class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)
        integer = 0

        rom = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        for i in range(n - 1):
            if rom[s[i + 1]] > rom[s[i]]:
                integer -= rom[s[i]]
            else:
                integer += rom[s[i]]

        integer += rom[s[n - 1]]

        return integer
