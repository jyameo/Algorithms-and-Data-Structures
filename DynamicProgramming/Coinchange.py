class CoinChange:

    def naiveApproach(self, amount, coins, index):
        if amount < 0:
            return 0
        if amount == 0:
            return 1

        if index == len(coins):
            return 0

        return self.naiveApproach(amount - coins[index], coins, index)\
            + self.naiveApproach(amount, coins, index + 1)

    def dpApproach(self, coins, amount):
        dp = [[0 for _ in range(amount+1)] for _ in range(len(coins)+1)]

        for i in range(len(coins) + 1):
            dp[i][0] = 1

        for i in range(1, len(coins)+1):
            for j in range(1, amount + 1):
                if coins[i-1] <= j:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]
max_amount = 500
coins = [1, 2, 3]
coinChange = CoinChange()
from time import time
t1 = time()
print(coinChange.naiveApproach(max_amount, coins, 0))
print('Naive recursion took: {} seconds'.format(time() - t1))
t1= time()
print(coinChange.dpApproach(coins, max_amount))
print('Dynamic programming took: {} seconds'.format(time() - t1))
