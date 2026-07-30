class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(row, col):
            if row < 0 or col < 0 or row > rows - 1 or col > cols - 1 or (row, col) in visited or grid[row][col] == '0':
                return

            visited.add((row, col))

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '0' or (row,col) in visited:
                    continue
                islands += 1
                dfs(row, col)
        return islands
                 

        