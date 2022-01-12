class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        string = list(s)

        max_length = 0
        substring = ""

        for count,characters in enumerate(string):

            left = count
            right = count
            
            while left>=0 and right < len(string) and string[left]==string[right]:

                curlength = (right-left)+1
 

                if curlength > max_length:
                    max_length = curlength
                    substring = "".join(string[left:right+1])

                left = left-1

                right = right+1
                
        
        for count,characters in enumerate(string):

            left = count
            right = count+1
            
            while left>=0 and right < len(string) and string[left]==string[right]:

                curlength = (right-left)+1
 

                if curlength > max_length:
                    max_length = curlength
                    substring = "".join(string[left:right+1])

                left = left-1

                right = right+1

        return(substring)