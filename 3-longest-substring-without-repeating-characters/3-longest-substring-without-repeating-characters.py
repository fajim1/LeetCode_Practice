class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == " ":
            return 1
        if s == "":
            return 0 
        left_window = 0
        right_window = 1
        
        num = 1
    
        max_s_l = 1
        
        sub_s = s[left_window:right_window]
        
        while num<len(s):
            
            if s[num] in sub_s:
                print("left1",sub_s,s[num],max_s_l)
                left_window = left_window + 1
                
                sub_s = s[left_window:right_window]
                
                if max_s_l < len(sub_s):
                    max_s_l = len(sub_s)
                    
                print("left2",sub_s,s[num],max_s_l)
                
                continue
                
            else:
                print("right1",sub_s,s[num],max_s_l)
                right_window=right_window+1
                
                sub_s = s[left_window:right_window]
                
                if max_s_l < len(sub_s):
                    max_s_l = len(sub_s)
                    
                print("right2",sub_s,s[num],max_s_l)
                    
                num = num+1
                
                continue
        
        return max_s_l
                
            
        
        