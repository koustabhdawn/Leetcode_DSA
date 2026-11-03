# class Solution:
#     def rec(self, n,dp) -> int:
#         if n<=1:
#             return n
#         if dp[n]!=-1:
#             return dp[n]
        
#         dp[n]=self.rec(n-1,dp)+self.rec(n-2,dp)
#         return dp[n]
#     def fib(self, n: int) -> int:
#         dp=[-1]*(n+1)
#         return self.rec(n,dp)

class Solution:
    def fib(self, n:int) -> int:
        if n<=1:
            return n
        dp=[0]*(n+1)
        dp[0]=0
        dp[1]=1
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]
        