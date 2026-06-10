class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maps = {}
        threshold = len(nums) / 2
        for i in nums:
            if i in maps:
                maps[i] += 1
            else:
                maps[i] = 1
        for i in maps:
            if maps[i] > threshold:
                return i
        return nums[0]