class RodCutting:

    def compute(self, length_of_rod, prices):
        dp = [[0 for _ in range(length_of_rod + 1)] for _ in range(len(prices)+1)]

        for i in range(1, len(prices) + 1):
            for j in range(1, length_of_rod + 1):
                if i <= j:
                    dp[i][j] = max(dp[i-1][j], prices[i-1] + dp[i][j-i])
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[-1][-1]
length_of_rod = 5
prices = [2, 5, 7, 3]

rodCutting = RodCutting()
print(rodCutting.compute(length_of_rod, prices))
