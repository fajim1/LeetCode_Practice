class Solution:
    def intToRoman(self, num: int) -> str:
        roman_value_dic = {"M":1000,"CM":900,"D":500,"CD":400,"C":100,"XC":90,"L":50,"XL":40,"X":10,"IX":9,"V":5,"IV":4,"I":1}
        roman = []
        
        def roman_letters(letter,num):
            letter_value = roman_value_dic[letter]
            letter_num = num//letter_value
            num = num - letter_num*letter_value
            for i in range(letter_num):
                roman.append(letter)
            
            return num
            
            
        for letters in roman_value_dic.keys():
            num = roman_letters(letters,num)
        
        return "".join(roman)

    
        