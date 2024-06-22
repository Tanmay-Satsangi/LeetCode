class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff

        while(b & mask != 0):
            carry = (a & b) << 1
            a = (a ^ b)
            b = carry

        return (a & mask) if b > 0 else a # because addition of two 32 bit integer may exceed 32 bit integer. So, 
                            # we have to do mask to make sure that integer does not exceed 32 bit integer