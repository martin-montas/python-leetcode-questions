class Solution:
    def combinationSum(self, candidates , target): 
        res = []
        def dfs(i,curr,total):
            if total == target:
                res.append(curr.copy())
                return

            if i >= len(candidates) or total >target:
                return
            curr.append(candidates[i]) 
            dfs(i,curr,total+candidates[i])
            curr.pop()
            dfs(i+1,curr,total)
            
        dfs(0,[],0)
        return res


s = Solution()
candidates= [2,4]

target= 8
x = s.combinationSum(candidates,target)
print(x)

