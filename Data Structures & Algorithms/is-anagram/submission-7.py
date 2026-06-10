class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        lengthS = len(s)
        lengthT = len(t)
        if lengthS != lengthT:
            return False
        for letter in s:
            if letter in seen:
                seen[letter] += 1
            else:
                seen[letter] = 1
        for letter in t:
            if letter in seen:
                seen[letter] -= 1
            else:
                return False
            if seen[letter] < 0:
                    return False
        return True