class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        if len(s) != len(set(s)):
            return False
        
        charStack = []

        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                charStack.append(s[i])
            if charStack:
                if s[i] == ')' and charStack[-1] == '(':
                    charStack.pop()
                    continue

                if s[i] == '}' and charStack[-1] == '{':
                    charStack.pop()
                    continue

                if s[i] == ']' and charStack[-1] == '[':
                    charStack.pop()
                    continue
            
        if len(charStack) == 0:
            return True
        else: 
            return False

    




        