class Solution:
    def climbStairs(self, n):
        
        memo = {}
        for  i in range(0,n+1):
            memo[i] = None

        def helper(n,memo):

        #### TODO:tHIS IS JUST RECUSION TRY USING DP SOON!!!!!!!!!
            if n >= 0:
                if memo[n] != None:
                    return memo[n]
                    
                if n == 0:
                    return 1

                one = helper(n-1,memo)
                two = helper(n-2,memo)
                
                memo[n] = one +two
                return one + two
                

            else:
                return 0

        rest = helper(n,memo)
        return rest







s = Solution()

n = 38

x = s.climbStairs(n)
print(x)
