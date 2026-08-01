class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        hashmap = {}
        output = []
        size = len(grid) * len(grid[0]) 
        for i in range(1, size + 1):
            hashmap[i] = 0
        for row in grid:
            for col in row:
                hashmap[col] += 1
                if hashmap[col] > 1:
                    output.append(col)
        for key in hashmap:
            if hashmap[key] < 1:
                output.append(key)
        
        return output
                
                


