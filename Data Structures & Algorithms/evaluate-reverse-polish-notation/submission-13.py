class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        #The operands may be integers or the results of other operations.

        #Assume that division between integers always truncates toward zero. 
        

        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(token))
        
        return stack[0]