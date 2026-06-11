class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        result = []
        for str in strs:
            sort = "".join(sorted(str))
            if sort in seen:
                seen[sort].append(str)
            else:
                seen[sort] = [str]
        for anagrams in seen.values():
            result.append(anagrams)
        return result