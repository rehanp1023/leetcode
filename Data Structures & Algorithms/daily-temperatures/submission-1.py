class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        length = len(temperatures)
        result = [0] * length


        for i in range(length):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                days = i - index
                result[index] = days
            stack.append(i)
        
        return result
