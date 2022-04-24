class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == None or len(s) <1:
            return ""

        start = 0
        end = 0

        for i in range(0,len(s)):
            len1 = check_for_palindrome(s,i,i)
            len2 = check_for_palindrome(s,i,i+1)
            _len = max(len1,len2)

            if _len > end - start:
                start = i-((_len-1)/2)
                end = i+(_len/2)

        return s[start:end+1]


def check_for_palindrome(s,left,right):
    if s == None or left > right:
        return 0
    while (left >=0 and right < len(s)) and (s[left] == s[right]):
        left -= 1
        right += 1

    return right - left -1

c = Solution()

s = "dabad"
x = c.longestPalindrome(s)

print(x)
