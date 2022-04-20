class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for char in s:
            if char == '(':
                stack.append(')')

            elif char == '[':
                stack.append(']')

            elif char == '{':
                stack.append('}')

            elif len(stack) == 0 or stack.pop() != char:
                return False

        if not stack:
            return True
        else:
            return False 


x= Solution()
s = "(())"
s  = x.isValid(s)

print(s)
