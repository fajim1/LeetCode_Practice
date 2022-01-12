class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        
        max_conf_room = 0
        conf_room = 0
        
        sorted_intervals = sorted(intervals,key=lambda x: x[0])
        
        start = []
        end = []
        
        for count in sorted_intervals:
            start.append(count[0])
            end.append(count[1])

        end = sorted(end)
        
        print(start)
        print(end)
        
        
        while True:
            if start[0] < end[0]:
                start.pop(0)
                conf_room +=1
                if conf_room > max_conf_room:
                    max_conf_room = conf_room
                
            else:
                end.pop(0)
                conf_room-=1
                if conf_room > max_conf_room:
                    max_conf_room = conf_room
                
            if not start:
                return max_conf_room 
        