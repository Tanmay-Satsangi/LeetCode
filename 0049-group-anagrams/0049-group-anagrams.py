from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                val = ord(c) - ord('a')
                count[val] += 1

            # In python, we need the tuple as a key because we cannot use list as the key of dictionary. Otherwise it throws an error: TypeError: unhashable type: 'list'.

            # BUT IN ROR, WE CAN USE LIST AS THE KEY OF DICTIONARY
            ans[tuple(count)].append(s) 

        
        return list(ans.values())
