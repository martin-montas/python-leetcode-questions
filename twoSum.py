class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
            for i in range(0,len(nums)):

                var = target - nums[i]
                if (var in nums):
                    if (i == nums.index(var)):
                        continue
                    return([i,nums.index(var)])
                
