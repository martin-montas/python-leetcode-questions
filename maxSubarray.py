class Solution:
    def maxSubArray(self, nums: [int]) -> int:
            _max = nums[0]
            _other = nums[0]
            for i in range(1,len(nums)):

                _max = max(_max + nums[i], nums[i])

                _other = max(_other, _max)
            return _other
