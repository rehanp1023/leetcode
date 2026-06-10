class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        for index, number in enumerate(nums):
            difference = target - number
            if difference in numbers:
                return [numbers[difference], index]
            else:
                numbers[number] = index
        return False