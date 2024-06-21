# https://www.youtube.com/watch?v=KOD2BFauQbA

class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = []
        lst = self.backtrack(n)

        for l in lst:
            decimal_num = int(l, 2) #convert binary to decimal
            res.append(decimal_num)
        return res

    def backtrack(self, n):
        if n == 1:
            lst = ['0', '1']
            return lst

        curr = self.backtrack(n - 1)

        lst = []

        for i in range(len(curr)):
            print("inside 1st for loop")
            lst.append('0' + curr[i])

        for i in range(len(curr) - 1, -1, -1):
            lst.append('1' + curr[i])
        
        return lst


        


                