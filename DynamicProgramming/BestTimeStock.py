class BestTimeStockDP_1(object):
    def at_most_one_transaction(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) < 2:
            return 0
            
        dp = [-1] * len(prices)
        dp[0] = 0
        
        min_price = prices[0]
        
        for i in range(1, len(prices)):
            dp[i] = max(dp[i-1], prices[i] - min_price)
            min_price = min(min_price, prices[i])
            
        return dp[-1]

class BestTimeStockDP_2(object):
    def at_most_one_transaction(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) < 2:
            return 0
            
        max_profit = 0
        min_price = prices[0]
        
        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i] - min_price)
            min_price = min(min_price, prices[i])
            
        return max_profit
        

class BestTimeStockGreedy(object):
    def multiple_transactions(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) < 2:
            return 0
            
        result = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i-1] > 0:
                result += prices[i] - prices[i-1]
            
        return result
        
class BestTimeStockDP(object):
    def at_most_two_transaction(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) < 2:
            return 0
        
        dp = [-1] * len(prices)
        dp[0] = 0
        
        valley = prices[0]
        
        for i in range(1, len(prices)):
            dp[i] = max(dp[i-1], prices[i] - valley)
            valley = min(valley, prices[i])
            
        peak = prices[-1]
        for i in range(len(prices)-2, -1, -1):
            if peak > prices[i]:
                dp[i] += max(0, peak - prices[i])
            peak = max(peak, prices[i]) 
            
        return max(dp)
        
class BestTimeStockDP_Greedy(object):
    def at_most_k_transaction(self, k, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) < 2:
            return 0
            
        if k * 2 >= len(prices):
            return BestTimeStockGreedy().multiple_transactions(prices)
        
        dp = [-1] * (2 * k + 1)
        dp[0] = 0
        
        for i in range(len(prices)):
            for j in range(1, min(2 * k, i + 1) + 1):
                if j % 2 == 0:
                    dp[j] = max(dp[j], dp[j - 1] + prices[i])
                else:
                    dp[j] = max(dp[j], dp[j - 1] - prices[i])
        
        return dp[-1]

assert BestTimeStockDP_1().at_most_one_transaction([7, 1, 5, 3, 6, 4]) == 5
print("BestTimeStockDP_1 <= 1 transaction: " + str(BestTimeStockDP_1().at_most_one_transaction([7, 1, 5, 3, 6, 4])))

assert BestTimeStockDP_2().at_most_one_transaction([7, 1, 5, 3, 6, 4]) == 5
print("BestTimeStockDP_2 <= 1 transaction: " + str(BestTimeStockDP_2().at_most_one_transaction([7, 1, 5, 3, 6, 4])))

assert BestTimeStockGreedy().multiple_transactions([7, 1, 5, 3, 6, 4]) == 7
print("BestTimeStockGreedy - multiple transactions: " + str(BestTimeStockGreedy().multiple_transactions([7, 1, 5, 3, 6, 4])))

assert BestTimeStockDP().at_most_two_transaction([7, 1, 5, 3, 6, 4]) == 7
print("BestTimeStockDP <= 2 transactions: " + str(BestTimeStockDP().at_most_two_transaction([7, 1, 5, 3, 6, 4])))

assert BestTimeStockDP_Greedy().at_most_k_transaction(1, [7, 1, 5, 3, 6, 4]) == 5
assert BestTimeStockDP_Greedy().at_most_k_transaction(2, [7, 1, 5, 3, 6, 4]) == 7
print("BestTimeStockDP_Greedy <= k transactions: " + str(BestTimeStockDP_Greedy().at_most_k_transaction(4, [7, 1, 5, 3, 6, 4])))