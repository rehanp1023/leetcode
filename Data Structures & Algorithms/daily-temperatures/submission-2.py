class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        hashmap = defaultdict(deque)
        
        for i, temp in enumerate(temperatures):
            hashmap[temp].append(i)
        
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1]:
                val = stack.pop()
                index = hashmap[val].popleft()
                result[index] = i - index
            stack.append(temp)
        
        return result