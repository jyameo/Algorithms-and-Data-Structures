class UniqueBstDFS(object):
    def tree_number(self, n):
        if n <= 1:
            return 1
        
        def dfs(l,r):
            if l >= r:
                return 1
            nways = 0
            for i in range(l,r+1):
                nways += dfs(l,i-1) * dfs(i+1,r)
            return nways
        return dfs(0,n-1)
        
class UniqueBstDFS_Cache(object):
    def tree_number(self, n):
        if n <= 1:
            return 1
        
        cache = [-1] * (n+1)
        
        def dfs(l,r):
            if l >= r:
                return 1
            if cache[r-l] != -1:
                return cache[r-l]
            nways = 0
            for i in range(l,r+1):
                nways += dfs(l,i-1) * dfs(i+1,r)
            cache[r-l] = nways
            return nways
        return dfs(0,n-1)
        
class UniqueBstDP(object):
    def tree_number(self, n):
        if n <= 1:
            return 1
        
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2,n+1):
            for j in range(i):
                dp[i] += dp[j] * dp[i-j-1]
        
        return dp[-1]
        

print("UniqueBst DFS: " + str(UniqueBstDFS().tree_number(3)))
print("UniqueBst DFS CACHE: " + str(UniqueBstDFS_Cache().tree_number(3)))
print("UniqueBst DP: " + str(UniqueBstDP().tree_number(3)))
