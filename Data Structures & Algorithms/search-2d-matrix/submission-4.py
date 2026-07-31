class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        
        top, bottom = 0, m - 1
        while top <= bottom:
            mid = (top + bottom) // 2
            if target < matrix[mid][0]:
                bottom = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                # Target could be in this row
                # Step 2: Binary search in this row
                left, right = 0, n - 1
                while left <= right:
                    col_mid = (left + right) // 2
                    if matrix[mid][col_mid] == target:
                        return True
                    elif matrix[mid][col_mid] < target:
                        left = col_mid + 1
                    else:
                        right = col_mid - 1
                return False
        
        return False