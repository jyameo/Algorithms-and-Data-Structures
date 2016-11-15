class Knapsack:

    def __init__(self, num_of_items, capacity, weight_of_items, profit_of_items):
        self.num_of_items = num_of_items
        self.capacity = capacity
        self.weight_of_items = weight_of_items
        self.profit_of_items = profit_of_items
        self.items_taken = [[0 for x in range(capacity+1)] for x in range(num_of_items + 1)]
        self.dp = [[0 for x in range(capacity+1)] for x in range(num_of_items + 1)]

    def compute(self):
        for i in range(1, self.num_of_items + 1):
            for w in range(1, self.capacity + 1):

                not_take = self.dp[i-1][w]
                take = 0
                if self.weight_of_items[i-1] <= w:
                    take = self.profit_of_items[i-1] + self.dp[i-1][w - self.weight_of_items[i-1]]

                self.dp[i][w] = max(take, not_take)

                if take > not_take:
                    self.items_taken[i][w] = 1
                else:
                    self.items_taken[i][w] = 0
        self.total = self.dp[-1][-1]

    def printResult(self):
        print("Total benefit: {}".format(self.total))

        w = self.capacity

        for i in range(self.num_of_items, 0, -1):
            if self.items_taken[i][w] == 1:
                print('- item # {} with value {}'.format(i, self.profit_of_items[i-1]))
                w = w - self.weight_of_items[i-1]

num_of_items = 5
capacity = 10
weight_of_items = [1, 2, 3, 4, 5]
profit_of_items = [1, 3, 4, 5, 6]


knapsack = Knapsack(num_of_items, capacity, weight_of_items, profit_of_items)
knapsack.compute()
knapsack.printResult()
