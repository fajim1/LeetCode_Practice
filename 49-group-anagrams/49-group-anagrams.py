class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_dic = {}
        
        for words in strs:
            sorted_word = sorted(words)
            sorted_word = "".join(sorted_word)
            
            if sorted_word not in anagram_dic:
                anagram_dic[sorted_word] = [words]
                
            else:
                anagram_dic[sorted_word].append(words)
                
        output_list = []
        
        for values in anagram_dic.values():
          
            output_list.append(values)

        
        return(output_list)
                