class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)
        sum_of_n = ((n**2)+n)//2
        
        
        return(sum_of_n-sum(nums))
        

        