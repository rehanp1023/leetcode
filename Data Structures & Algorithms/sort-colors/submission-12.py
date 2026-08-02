class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hashmap = {}
        for num in nums:
            if hashmap.get(num):
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        index = 0
        for color in range(3):
            if color in hashmap:
                for i in range(hashmap[color]):
                    nums[index] = color
                    index += 1

            