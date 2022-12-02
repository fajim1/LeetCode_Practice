class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        area = 0
        
        print(height)
        
        left = 0
        right = len(height)-1
        
        while left<=right:
     
            tmp_area = min(height[left],height[right])*(right-left)
        
            area = max(area,tmp_area)

            
            if height[left] <= height[right]:
                left = left+1
            else:
                right = right - 1
                    
        return area
                

