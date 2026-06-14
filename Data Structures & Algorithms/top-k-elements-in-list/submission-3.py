class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        result = []
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        
        number = 0
        while number < k:
            maximum = max(frequency.values())
            for key in frequency:
                if frequency[key] == maximum:
                    result.append(key)
                    frequency[key] = 0
                    number += 1
        return result
