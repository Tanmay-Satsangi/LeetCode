class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if s[0] in [")", "}", "]"]:
            return False

        for br in s:
            if stack and (br == "}" and stack[-1] == "{" or br == ")" and stack[-1] == "(" or br == "]" and stack[-1] == "["):
                stack.pop()

            else:
                stack.append(br)

        return stack == []

        