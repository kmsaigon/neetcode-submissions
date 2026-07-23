class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        word1 = {}
        word2 = {}

        for letter in s:
            word1[letter] = word1.get(letter, 0) + 1

        for letter in t:
            word2[letter] = word2.get(letter, 0) + 1

        return Counter(word1) == Counter(word2)
        