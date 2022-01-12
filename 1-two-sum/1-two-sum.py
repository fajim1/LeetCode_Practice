class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dic = {}
        
        indices = []
        
        for index,value in enumerate(nums):
            
            dic[value] = index
            
        for index,value in enumerate(nums):
            diff = target-value
            if diff in dic.keys() and dic[diff]!=index:
                indices= [index,dic[diff]]
                return indices
                
            
        
        
#         val = []
#         idx = []
        
#         for count1,value1 in enumerate(nums):
#             flag = True
#             for count2,value2 in enumerate(nums):
#                 if count1==count2:
#                     continue
#                 if value1 + value2 == target:
#                     val.append(value1)
#                     val.append(value2)
#                     idx.append(count1)
#                     idx.append(count2)
                    
#                     flag = False
#             if flag == False:
#                 break
                    
#         print(val)
#         print(idx)
        
#         return idx
            
            

        
        