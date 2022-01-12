class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        boxTypes = sorted(boxTypes,key=lambda x:x[1],reverse=True)
        
        units = 0
        
        for all_boxes in boxTypes:
            
            if truckSize <= 0:
                break
            
            if all_boxes[0] < truckSize:
                units = units + all_boxes[0]*all_boxes[1]
                truckSize = truckSize - all_boxes[0]
                
            else:
                units = units + (truckSize)*all_boxes[1]
                truckSize = truckSize - all_boxes[0]
        
        
        return units