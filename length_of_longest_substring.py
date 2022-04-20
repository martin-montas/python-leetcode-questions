class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int_
        """
        if not s:
            return 0

        sub_s = set() 
        count = 0
        _subs = ""

        for i in range(0,len(s)):
            if s[i] not in _subs:
                _subs += s[i]
                count += 1
                sub_s.add(count)
            for j in range(i+1,len(s)):
                if s[j]  not in _subs:
                    count += 1
                    _subs += s[j]
                    sub_s.add(count)
                else:
                    count = 0
                    _subs = ""
                    break

        print(max(sub_s))

s = "dvdf"
x = Solution() 

res = x.lengthOfLongestSubstring(s)

print(res)


                """
                print("###################################################3333")
                print("current i val ",s[i]," current count ",count,"current set ",sub_s)
                print("current str ",_subs)
                """
