class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re



        
        s = s.lower()
        s = re.sub(r'[^\w\s]','',s)
        s = s.replace(" ","")
        s = s.replace("_","")
        
        start = 0
        end = len(s)-1
        
        print(s)
        
        while start < end:
            
            if s[start] == s[end]:
                start +=1
                end -=1
            
            else:
                return False
            
        return True
        