class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums)-1
        mid = (left+right)//2
        
        count = 0
        while count<=15:
            
            if nums[mid] < target:
                left = mid+1
            
            elif nums[mid] > target:
                right = mid
                
            else:
                return mid
            
            mid = (left+right)//2
            count+=1
        
        return -1
                
            