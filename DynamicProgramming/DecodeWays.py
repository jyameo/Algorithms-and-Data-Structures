class DecodeWaysDFS(object):
    def decode(self, s):
        if not s or len(s) == 0:
            return 0
        
        def dfs(pos):
            if pos < len(s) and s[pos] == '0':
                return 0
                
            if pos == len(s):
                return 1
            
            nway = dfs(pos+1)
            val = 0
            if pos + 1 < len(s):
                val = int(s[pos:pos+2])
            if val >= 10 and val <= 26:
                nway += dfs(pos+2)
            return nway
        
        return dfs(0)
        
        
class DecodeWaysDFS_Cache(object):
    def decode(self, s):
        if not s or len(s) == 0:
            return 0
        cache = [-1] * (len(s)+1)
        def dfs(pos):
            if pos < len(s) and s[pos] == '0':
                return 0
                
            if pos == len(s):
                return 1
                
            if cache[pos] != -1:
                return cache[pos]
            
            nway = dfs(pos+1)
            val = 0
            if pos + 1 < len(s):
                val = int(s[pos:pos+2])
            if val >= 10 and val <= 26:
                nway += dfs(pos+2)
            cache[pos] = nway
            return nway
        
        return dfs(0)
        
class DecodeWaysBFS(object):
    def decode(self, s):
        if not s or len(s) == 0:
            return 0
            
        q = []
        result = []
        q.append(0)
        nway = 0
        while q:
            cur = q.pop(0)
            
            if cur == len(s):
                nway += 1
            elif s[cur] == 0:
                continue
            else:
                q.append(cur+1)
                val = 0
                if cur + 1 < len(s):
                    val = int(s[cur:cur+2])
                if val >= 10 and val <= 26:
                    q.append(cur+2)
        return nway
        
class DecodeWaysDP_1(object):
    def decode(self, s):
        if not s or len(s) == 0:
            return 0
        
        dp = [-1] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0
        
        for i in range(1, len(s)):
            if s[i] != '0':
                dp[i+1] = dp[i]
            val = int(s[i-1:i+1])
            if val >= 10and val <= 26:
                dp[i+1] += dp[i-1]
        
        return dp[-1]
        
class DecodeWaysDP_2(object):
    def decode(self, s):
        if not s or len(s) == 0:
            return 0

        f0 = 1
        f1 = 1 if s[0] != '0' else 0
        
        f2 = f1
        
        for i in range(1, len(s)):
            if s[i] != '0':
                f2 = f1
            val = int(s[i-1:i+1])
            if val >= 10and val <= 26:
                f2 += f0
        
        return f2
            
            
            
            
            
print("DecodeWays DFS: " + str(DecodeWaysDFS().decode("121212")))
print("DecodeWays BFS: " + str(DecodeWaysBFS().decode("121212")))
print("DecodeWays DFS CACHE: " + str(DecodeWaysDFS_Cache().decode("121212")))
print("DecodeWays DP: " + str(DecodeWaysDP_1().decode("121212")))
print("DecodeWays DP 2: " + str(DecodeWaysDP_1().decode("121212")))