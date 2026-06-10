class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        for letter in s:
            letters[letter] = 0
        for letter in s:
            letters[letter] += 1
        for letter in t:
            if letter not in s:
                return False
            letters[letter] -= 1
        for times in letters.values():
            if times != 0:
                return False
        return True
        