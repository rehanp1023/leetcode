class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        length = len(strs[0])
        for str in strs:
            new = len(str)
            if new < length:
                length = new
        for i in range(length):
            for str in strs:
                if str[i] != strs[0][i]:
                    return prefix
            prefix += strs[0][i]
        return prefix
