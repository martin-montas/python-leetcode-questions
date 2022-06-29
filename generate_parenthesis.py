class Solution:
    def generateParenthesis(self,n) :

        stack = []
        res = []


        def backtack(open,close):
            if open == close == n:
                res.append("".join(stack))
                return
            
            if open < n:
                stack.append("(")
                backtack(open+1,close)
                stack.pop()

            if close < open:
                stack.append(")")
                backtack(open,close+1)
                stack.pop()


        backtack(0,0)
        return res

n = 3

s = Solution()
x = s.generateParenthesis(n)
print(x)
