class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = [0] * 2 * len(nums)
        for i in range(length * 2):
            ans[i] = nums[i % length]
        return ans