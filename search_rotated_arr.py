class Solution:
    def search(self, nums , target )  :
        
        l, r = 0 , len(nums) -1
        res =-1

        while l <= r:
            mid = (l + r) //2
            if target == nums[mid]:
                return mid

            elif nums[l] <= nums[mid]:
                if target <= nums[mid] and target >= nums[l]:
                    r = mid -1
                else:
                    l = mid + 1

            elif nums[mid] <= nums[r]:
                if target <= nums[r] and target >= nums[mid]:
                    l = mid + 1
                else:
                    r = mid -1
            else:
                break

        return res
