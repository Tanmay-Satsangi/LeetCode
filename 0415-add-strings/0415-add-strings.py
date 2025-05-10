class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1 = len(num1) - 1
        n2 = len(num2) - 1


        carry = 0
        ans = ""

        while (n1 >= 0 or n2 >= 0):
            if (n1 >= 0 and n2 >= 0):
                # In ruby '3'.ord - '0'.ord
                sums = (ord(num1[n1]) - ord('0')) + (ord(num2[n2]) - ord('0')) + carry
                ans += str(sums % 10)
                carry = sums // 10

                n1 -= 1
                n2 -= 1
            
            elif (n1 >= 0):
                sums = (ord(num1[n1]) - ord('0')) + carry
                ans += str(sums % 10)
                carry = sums // 10

                n1 -= 1

            else:
                sums = (ord(num2[n2]) - ord('0')) + carry
                ans += str(sums % 10)
                carry = sums // 10

                n2 -= 1

        if carry:
            ans += str(carry)
 
        return ans[::-1]
