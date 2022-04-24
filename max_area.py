class Solution:
    def maxArea(self, height):

        _max = 0
        l = 0
        r = len(height) -1

        while l < r:
            _min  = min(height[l],height[r])

            _amount = (r - l) * _min

            if _amount > _max:
                _max = _amount

            if height[l] > height[r]:

                r -= 1
            else:
                l += 1

        return _max


height = [2,4,5,6,7,8,6,7]

s = Solution()
x = s.maxArea(height)

print(x)
