class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        # if s[0] in [")", "}", "]"]:
        #     return False

        for br in s:
            if stack and (br == "}" and stack[-1] == "{" or br == ")" and stack[-1] == "(" or br == "]" and stack[-1] == "["):
                stack.pop()

            # elif stack == [] and br in [")", "}", "]"]:
            #     return False
            else:
                stack.append(br)

        return stack == []

        