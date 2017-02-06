class HouseRobberDFS(object):
    def rob(self, houses):
        if not houses or len(houses) == 0:
            return 0
        
        def dfs(pos):
            if pos >= len(houses):
                return 0
                
            opt1 = houses[pos] + dfs(pos+2)
            opt2 = dfs(pos+1)
            
            return max(opt1, opt2)
        
        return dfs(0)
        

class HouseRobberDFS_Cache(object):
    def rob(self, houses):
        if not houses or len(houses) == 0:
            return 0
        
        cache = [-1] * (len(houses))
        
        def dfs(pos):
            if pos >= len(houses):
                return 0
            if cache[pos] != -1:
                return cache[pos]
            opt1 = houses[pos] + dfs(pos+2)
            opt2 = dfs(pos+1)
            
            cache[pos] = max(opt1, opt2)
            return cache[pos]
        
        return dfs(0)  
        
class HouseRobberDP_1(object):
    def rob(self, houses):
        if not houses or len(houses) == 0:
            return 0
        
        dp = [-1] * (len(houses))
        dp[0] = houses[0]
        dp[1] = max(houses[0], houses[1])
        
        for i in range(2, len(houses)):
            opt1 = houses[i] + dp[i-2]
            opt2 = dp[i-1]
            
            dp[i] = max(opt1, opt2)
        return dp[-1]
        
        
class HouseRobberDP_2(object):
    def rob(self, houses):
        if not houses or len(houses) == 0:
            return 0
        
        f0 = houses[0]
        f1 = max(houses[0], houses[1])
        f2 = f1
        for i in range(2, len(houses)):
            opt1 = houses[i] + f0
            opt2 = f1
            
            f2 = max(opt1, opt2)
            f0 = f1
            f1 = f2
            
        return f2


print("House Robber DFS: " + str(HouseRobberDFS().rob([1,5,4,1,3])))
print("House Robber DFS Cache: " + str(HouseRobberDFS_Cache().rob([1,5,4,1,3])))
print("House Robber DP 1: " + str(HouseRobberDP_1().rob([1,5,4,1,3])))
print("House Robber DP 2: " + str(HouseRobberDP_2().rob([1,5,4,1,3])))