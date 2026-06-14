class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = {}
        for num in nums:
            if num in colors:
                colors[num] += 1
            else:
                colors[num] = 1
        index = 0
        for color in range(3):
            if color in colors:    
                for i in range(colors[color]):
                    nums[index] = color
                    index += 1