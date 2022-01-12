class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        factor_list = []
        
        for i in range(1,floor(sqrt(n))+1):
            if n%i == 0:
                factor_list.append(i)
                
                i2 = n//i
                
 
                
                if i2==i:
                    continue
                else:
                    factor_list.append(i2)

        factor_list = sorted(factor_list)
        if k > len(factor_list):
            return -1
        else:
            return factor_list[k-1]
        
        