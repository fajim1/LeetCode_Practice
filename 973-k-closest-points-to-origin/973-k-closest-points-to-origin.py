class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        dist_index = []
        
        for count,coords in enumerate(points):
            distance = sqrt(coords[0]**2 + coords[1]**2)
            
            dist_index.append([distance,count])
            
        dist_index = sorted(dist_index,key = lambda x:x[0])
        
        ordered_coords = []
        
        
        for i in range(0,k):
            index = dist_index[i][1]
            coords = points[index]
            ordered_coords.append(coords)
            
        
        print(ordered_coords)
        
        return(ordered_coords)
        
        
            
        