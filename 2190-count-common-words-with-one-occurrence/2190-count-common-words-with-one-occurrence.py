class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        dict_word1 = {}
        dict_word2 = {}
        common_words = []

        for word in words1:
            if word not in dict_word1:
                dict_word1[word] = 1
            else:
                dict_word1[word] += 1

        for word in words2:
            if word not in dict_word2:
                dict_word2[word] = 1
            else:
                dict_word2[word] += 1

        for k, v in dict_word1.items():
            if dict_word1[k] == 1 and (k in dict_word2 and dict_word2[k] == 1):
                common_words.append(k)

        return len(common_words)
                


        