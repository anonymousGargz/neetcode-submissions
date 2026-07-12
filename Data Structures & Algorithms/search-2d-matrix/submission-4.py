class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1
        row_found = -1
        while top <= bottom:
            mid = (top + bottom) // 2
            if matrix[mid][0] == target or matrix[mid][-1] == target:
                return True
            elif matrix[mid][0] < target and matrix[mid][-1] > target:
                row_found = mid
                break
            elif matrix[mid][-1] < target:
                top = mid + 1
            else:
                bottom = mid - 1

        if row_found == -1:
            return False

        left, right = 0, len(matrix[0]) - 1
        while left <= right:
            midP = (left + right) // 2
            if matrix[row_found][midP] == target:
                return True
            elif matrix[row_found][midP] < target:
                left = midP + 1
            else:
                right = midP - 1
        return False