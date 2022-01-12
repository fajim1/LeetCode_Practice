class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        sorted_intervals = sorted(intervals,key=lambda x: x[0])
        
        for count in range(1,len(sorted_intervals)):
            if sorted_intervals[count-1][1] > sorted_intervals[count][0]:
                return False
            
        return True
                
        