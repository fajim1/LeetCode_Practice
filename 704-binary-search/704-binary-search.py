class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums)-1
        mid = (left+right)//2
        
        countl = 0
        countr = 0
        while countl<=2 and countr <=2:
            
            if nums[mid] < target:
                left = mid+1
            
            elif nums[mid] > target:
                right = mid
                
            else:
                return mid
            
            mid = (left+right)//2
            
            if mid==left:
                countl+=1
            elif mid == right:
                countl+=1
            
        return -1
                
            