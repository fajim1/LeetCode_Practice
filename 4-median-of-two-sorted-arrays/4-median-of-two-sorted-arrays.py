class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        print(nums1+nums2)
        
        comb_nums = nums1+nums2
        comb_nums = sorted(comb_nums)
        
        if len(comb_nums)%2 == 1:   # [1,2,3,4,5,6,7]
            return(comb_nums[len(comb_nums)//2])
        
        else: # [1,2,3,4,5,6]
            med1 = comb_nums[len(comb_nums)//2]
            med2 = comb_nums[(len(comb_nums)//2)-1]
            
            return (med1+med2)/2
