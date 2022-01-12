class Solution:
    def romanToInt(self, s: str) -> int:
        
        roman_value_dic = {"M":1000,"CM":900,"D":500,"CD":400,"C":100,"XC":90,"L":50,"XL":40,"X":10,"IX":9,"V":5,"IV":4,"I":1}

        s_list = list(s)
        
        num = 0
        
        while s_list:
            two_l = None
            
            if len(s_list)>=2:
                two_l = s_list[:2].copy()
                two_l = "".join(two_l)
            
            if two_l == "CM" or two_l == "CD" or two_l == "XC" or two_l == "XL" or two_l == "IX" or two_l == "IV":
                num = num + roman_value_dic[two_l]
                
                s_list.pop(0)
                s_list.pop(0)
            else:
                num = num + roman_value_dic[s_list[0]]
                s_list.pop(0)
                
        return(num)
            
            