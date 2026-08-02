class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        hashmap = defaultdict(list)
        for i, temperature in enumerate(temperatures):
            hashmap[temperature].append(i)


        for i, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1]:
                val = stack.pop()
                index = hashmap[val].pop(0)
                days = i - index
                result[index] = days
            stack.append(temperature)
        
        return result
