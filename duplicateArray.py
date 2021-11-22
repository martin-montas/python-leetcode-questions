class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        base = 0
        nexts = 0
        while True:
            if not nums:
                break
            nexts = base +1
            if len(nums) == (base+1):
                break
            elif nums[base] == nums[nexts]:
                nums.remove(nums[nexts])
                
            elif nums[base] != nums[nexts]:
                base = base +1
                
        print(nums) 
