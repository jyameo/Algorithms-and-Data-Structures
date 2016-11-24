class Permutation:
    def permute(self, nums):
        self.result = []

        def dfs(start):
            if start == len(nums):
                self.result.append(nums[:])
                return

            for i in range(start, len(nums)):
                nums[i], nums[start] = nums[start], nums[i]
                dfs(start+1)
                nums[i], nums[start] = nums[start], nums[i]
        dfs(0)
        return self.result


class Combination:
    def combine(self, n, k):
        self.result = []
        self.count = 0

        def dfs(start, tmp):
            if self.count == k:
                self.result.append(tmp)
                return

            for i in range(start, n+1):
                self.count += 1
                dfs(i + 1, tmp + [i])
                self.count -= 1
        dfs(1, [])
        return self.result

    def combinationSum(self, candidates, target):
        self.result = set()
        n = len(candidates)

        def dfs(start, target, tmp):
            if target == 0:
                self.result.add(tuple(tmp))
                return
            for i in range(start, n):
                if target >= candidates[i]:
                    dfs(i, target - candidates[i],
                        tmp + [candidates[i]])
        dfs(0, target, [])
        return [sorted(x) for x in self.result]


class Subset(object):
    def compute(self, S):
        self.result = []

        def dfs(depth, start, tmp):
            if depth == len(S):
                self.result.append(tmp)
                return
            self.result.append(tmp)
            for i in range(start, len(S)):
                dfs(depth + 1, i + 1, tmp + [S[i]])
        dfs(0, 0, [])
        return self.result


class nQueens:
    def solveNQueens(self, n):
        # write your code here
        self.board = [-1] * n
        self.result = []

        def dfs(row, tmp):
            if row == n:
                self.result.append(tmp)
                return

            for col in range(n):
                if isValid(row, col):
                    self.board[row] = col
                    sol = '.' * n
                    dfs(row+1, tmp + [sol[:col] + 'Q' + sol[col+1:]])

        def isValid(row, col):

            for prev_row in range(row):
                if self.board[prev_row] == col or \
                        abs(row-prev_row) == abs(self.board[prev_row] - col):
                    return False
            return True

        dfs(0, [])
        return self.result

print('permunation: ' + str(Permutation().permute([1, 2, 3])))
print('combination: ' + str(Combination().combine(3, 2)))
print('combinationSum: ' + str(Combination().combinationSum([1, 2, 3], 4)))
print('Subset: ' + str(Subset().compute([1, 2, 3])))
print('nqueens: ' + str(nQueens().solveNQueens(4)))
