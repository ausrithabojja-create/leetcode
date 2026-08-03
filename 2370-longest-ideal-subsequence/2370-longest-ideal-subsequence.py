class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26
        for val in s:
            idx = ord(val) - ord('a')
            best = 0
            for i in range(max(0, idx-k), min(25, idx+k)+1):
                best = max(best, dp[i])
            dp[idx] = best + 1
        return max(dp) 

        