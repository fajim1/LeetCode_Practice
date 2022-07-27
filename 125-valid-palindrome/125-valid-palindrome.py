class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re

        
        s = s.lower()
        s = re.sub(r'\W+','',s)
        s = re.sub(r'_','',s)

        start = 0
        end = len(s)-1
        
        
        while start < end:
            
            if s[start] == s[end]:
                start +=1
                end -=1
            
            else:
                return False
            
        return True
        