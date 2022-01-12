import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        paragraph = paragraph.lower()
        banned_dic = {}
        
        for i in banned:
            banned_dic[i]=1
              
        paragraph = re.sub(r'[^\w\s]',' ',paragraph)
    
        p_list = paragraph.split(" ")
        
        print(p_list)
        
        dic = {}
        
        for words in p_list:
            
            if words.lower() in banned_dic.keys():
                continue
            
            if words == "":
                continue
            if words.lower() in dic.keys():
                dic[words.lower()] = dic[words.lower()]+1
            else:
                dic[words.lower()] = 1
                
        print(dic)
        return(max(dic, key=dic.get))
        