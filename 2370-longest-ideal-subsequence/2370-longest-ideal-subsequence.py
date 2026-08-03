class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26

        for ch in s:
            idx = ord(ch) - ord('a')
            best = 0

            for i in range(max(0, idx-k), min(25, idx+k)+1):
                best = max(best, dp[i])

            dp[idx] = best + 1

        return max(dp)
        # n=len(s)
        # dp=[1]*n
        # for m in range(n):
        #     for n in range(m):
        #         if abs(ord(s[m])-ord(s[n]))<=k:
        #             dp[m]=max(dp[m],dp[n]+1)
        # return max(dp) 

        