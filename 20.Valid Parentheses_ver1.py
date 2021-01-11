class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_bracket = ['{', '[', '('] 
        close_bracket = ['}', ']', ')'] 
        
        if len(s)%2 == 1:
            return False
        else:
            for i in s:
                if i in open_bracket: 
                    stack.append(i) 
                elif i in close_bracket:
                    if len(stack) <= 0:
                        return False
                    if open_bracket.index(stack.pop()) != close_bracket.index(i):
                        return False
            return len(stack) == 0