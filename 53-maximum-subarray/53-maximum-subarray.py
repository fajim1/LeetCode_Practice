class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        largest_sum = nums[0]
        
        temp_sum = 0
        
        for n in nums:
            
            if temp_sum<0:
                temp_sum=0
                
            temp_sum +=n
            
            largest_sum = max(largest_sum,temp_sum)
            
        return largest_sum
            
            
            
            
            