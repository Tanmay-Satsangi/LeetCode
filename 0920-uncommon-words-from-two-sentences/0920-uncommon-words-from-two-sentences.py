class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words = {}
        uncommon_words = []

        s1 = s1.split()
        s2 = s2.split()

        for s in s1:
            if s not in words:
                words[s] = 1
            else:
                words[s] += 1

        for s in s2:
            if s not in words:
                words[s] = 1
            else:
                words[s] += 1
        
        for k, v in words.items():
            if v == 1:
                uncommon_words.append(k)

        return uncommon_words
