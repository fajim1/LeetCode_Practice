class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1_hash = {}
        
        s2_hash = {}
        
        s1_len = len(s1)
        
        left = 0
        right = s1_len-1
        
        while right < len(s1):
        
            ch = s1[left:right+1]
            ch = sorted(ch)
            ch = "".join(ch)

            if ch in s1_hash.keys():
                s1_hash[ch]+=1
            else:
                s1_hash[ch]=1

            left+=1
            right+=1

            
            
        left = 0
        right = s1_len-1
        
        while right < len(s2):
        
            ch = s2[left:right+1]
            ch = sorted(ch)
            ch = "".join(ch)

            if ch in s2_hash.keys():
                s2_hash[ch]+=1
            else:
                s2_hash[ch]=1

            left+=1
            right+=1
        
                
        for key,value in s1_hash.items():
            
            if key in s2_hash.keys():
                continue

            else:
                return False
            
        return True