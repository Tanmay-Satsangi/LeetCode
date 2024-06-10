class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans_list = []

        for num in range(left, right + 1):
            string = str(num)

            if "0" not in string:
                divisible = True
                for s in string:
                    if num % int(s) != 0:
                        divisible = False

                if divisible:
                    ans_list.append(num)

        return ans_list