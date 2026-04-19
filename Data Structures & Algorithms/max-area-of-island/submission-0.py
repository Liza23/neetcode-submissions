class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        N = len(grid)        
        M = len(grid[0])        
        visited = [[False for i in range(M)] for i in range(N)]        

        def area(i, j):
            if i < 0 or j < 0 or i >= N or j >= M or not grid[i][j] or visited[i][j]:
                return 0
            visited[i][j] = True
            return 1 + area(i - 1, j) + area(i, j - 1) + area(i + 1, j) + area(i, j + 1)

        max_area = 0
        for i in range(N):            
            for j in range(M):                
                if grid[i][j] and not visited[i][j]:                    
                    max_area = max(max_area, area(i, j))
        return max_area