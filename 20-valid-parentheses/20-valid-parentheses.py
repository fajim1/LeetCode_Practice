class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        open_brk = ['(','{','[']
        close_brk = [')','}',']']

        
        for brk in s:
            
            if brk in open_brk:
                stack.append(brk)
            
            elif len(stack)==0 and brk in close_brk:
                return False
                
            else:
                if stack[-1]=='(' and brk == ')':
                    stack.pop()

                elif stack[-1]=='{' and brk == '}':
                    stack.pop()

                elif stack[-1]=='[' and brk == ']':
                    stack.pop()
                else:
                    return False        
            
        if stack:
            return False
        else:
            return True
                