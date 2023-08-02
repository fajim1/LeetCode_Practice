class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic_grams = {}
        
        for st in strs:
            if "".join(sorted(st)) in dic_grams.keys():
                dic_grams["".join(sorted(st))].append(st)
            else:
                dic_grams["".join(sorted(st))] = [st]
                
        output = []
        
        for key,value in dic_grams.items():
            output.append(value)
            
        return output