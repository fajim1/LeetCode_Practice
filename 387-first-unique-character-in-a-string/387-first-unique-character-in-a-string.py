class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        print(s)
        
        count_dic = {}
        
        list_string = list(s)
        
        for index, ch in enumerate(list_string):
            
            if ch not in count_dic.keys():
                count_dic[ch] = [1,index]
            
            else:
                
                count_dic[ch][0] += 1
                
        
        for key,value in count_dic.items():
            if value[0] == 1:
                return value[1]
        
        return -1