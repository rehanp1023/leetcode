class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        i = 0
        for num in nums:
            if num in seen:
                return True
            seen[num] = i
            i += 1
        return False