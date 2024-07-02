class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicts = {}
        dictt = {}

        for i in range(len(s)):
            if s[i] not in dicts:
                dicts[s[i]] = 1
            else: 
                dicts[s[i]] += 1
        
        for i in range(len(t)):
            if t[i] not in dictt:
                dictt[t[i]] = 1
            else: 
                dictt[t[i]] += 1

        return dicts == dictt
        