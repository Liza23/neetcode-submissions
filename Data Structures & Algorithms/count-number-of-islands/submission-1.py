class Solution:    
    def numIslands(self, grid: List[List[str]]) -> int:        
        num_island = 0        
        N = len(grid)        
        M = len(grid[0])        
        visited = [[False for i in range(M)] for i in range(N)]        

        def dfs(r, c):            
            if r < 0 or c < 0 or r >= N or c >= M or grid[r][c] == "0" or visited[r][c]:                
                return            
            visited[r][c] = True            
            dfs(r + 1, c)            
            dfs(r - 1, c)            
            dfs(r, c + 1)            
            dfs(r, c - 1)        

        for i in range(N):            
            for j in range(M):                
                if grid[i][j] == "1" and not visited[i][j]:                    
                    num_island += 1                    
                    dfs(i, j)        
        return num_island