from collections import Counter
class Solution:
    def containsDuplicate(self, nums: [int]) -> bool:
            dic = Counter(nums)
    
            ar = [x for x in dic if dic[x] > 1]
            if (ar):
                return( True)
            else:
                return( False)
