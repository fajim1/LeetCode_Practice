from collections import deque 
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        
        visited = set()
        
        num_islands = 0
        
        def bfs(r,c):
            
            queue = deque()
            
            queue.append((r,c))
            
            visited.add((r,c))
            
            while queue:
                
                row,col = queue.popleft()
                
                directions = [[0,1],[1,0],[0,-1],[-1,0]]
                
                for dr,dc in directions:
                    
                    new_row, new_col = row+dr,col+dc
                    
                    if (new_row in range(rows) and
                       new_col in range(cols) and 
                       (new_row,new_col) not in visited and
                       grid[new_row][new_col] == "1"):
                            
                            visited.add((new_row,new_col))
                            queue.append((new_row,new_col))
                
            
            
            
        for r in range(rows):
            for c in range(cols):
                
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    num_islands += 1 
                    
        
        return num_islands
            
        
        