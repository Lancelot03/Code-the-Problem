def uniquePaths(self, m: int, n: int) -> int:
        if m == n == 1:
            return 1
        dp=[[1]*m]*n
        for row in range(1, len(dp)):
            for col in range(1,len(dp[row])):
                dp[row][col]=dp[row-1][col]+ dp[row][col-1]
        return dp[-1][-1]
