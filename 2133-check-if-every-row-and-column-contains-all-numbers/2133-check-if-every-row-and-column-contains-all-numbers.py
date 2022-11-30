class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        n = len(matrix)
        
        for r in range(n):
            for c in range(n):
                if matrix[r][c] in rows[r] or matrix[r][c] in cols[c] or matrix[r][c] > n:
                    return False
                cols[c].add(matrix[r][c])
                rows[r].add(matrix[r][c])
        return True
            