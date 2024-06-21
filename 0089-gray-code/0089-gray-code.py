# https://www.youtube.com/watch?v=KOD2BFauQbA
class Solution:
    def grayCode(self, n: int) -> List[int]:
        binary_list = self.backtrack(n)

        #Convert the binary digits of lst into decimal 
        res = []

        for bin_list in binary_list:
            decimal_num = int(bin_list, 2)
            res.append(decimal_num)

        return res

    def backtrack(self, n):
        if n == 1:
            lst = ['0', '1']
            return lst

        curr = self.backtrack(n - 1)

        lst = []
        
        for i in range(len(curr)):
            lst.append('0' + curr[i])

        for i in range(len(curr) - 1, -1, -1):
            lst.append('1' + curr[i])

        return lst


        