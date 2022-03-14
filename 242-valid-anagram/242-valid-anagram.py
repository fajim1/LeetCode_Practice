class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        dic = {}
        
        for char in s:
         
            if char in dic.keys():
                dic[char] +=1
            else:
                dic[char] = 1
                
        print(dic)
        
        for char in t:
            
            if char in dic.keys():
                dic[char] -=1
                if dic[char]<0:
                    return False
            else:
                return False
        
        for vals in dic.values():
            if vals >0:
                return False
        
        
        return True