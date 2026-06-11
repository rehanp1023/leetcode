class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = {}
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        most = 0
        count = 0
        for key, value in seen.items():
            if value > count:
                most = key
                count = value
        return most