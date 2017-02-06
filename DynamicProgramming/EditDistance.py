class EditDistanceDFS(object):
    def compute(self, word1, word2):
        
        def dfs(pos1, pos2):
            if pos1 == len(word1) and pos2 == len(word2):
                return 0
            if pos1 == len(word1):
                return len(word2) - pos2
            if pos2 == len(word2):
                return len(word1) - pos1
                
            if word1[pos1] == word2[pos2]:
                return dfs(pos1+1, pos2+1)
            
            opt1 = dfs(pos1+1, pos2+1)
            opt2 = dfs(pos1+1,pos2)
            opt3 = dfs(pos1, pos2+1)
            
            tmp = min(opt1, opt2)
            return min(tmp, opt3) + 1
        
        return dfs(0,0)
      
        
class EditDistanceDFS_Cache(object):
    def compute(self, word1, word2):
        
        cache = [[-1] * (len(word2)) for _ in range(len(word1))]
        
        def dfs(pos1, pos2):
            if pos1 == len(word1) and pos2 == len(word2):
                return 0
            if pos1 == len(word1):
                return len(word2) - pos2
            if pos2 == len(word2):
                return len(word1) - pos1
                
            if cache[pos1][pos2] != -1:
                return cache[pos1][pos2]
                
            if word1[pos1] == word2[pos2]:
                return dfs(pos1+1, pos2+1)
            
            opt1 = dfs(pos1+1, pos2+1)
            opt2 = dfs(pos1+1,pos2)
            opt3 = dfs(pos1, pos2+1)
            
            tmp = min(opt1, opt2)
            cache[pos1][pos2] = min(tmp, opt3) + 1
            return cache[pos1][pos2]
        return dfs(0,0)
        

class EditDistanceDP(object):
    def compute(self, word1, word2):
        dp = [[-1] * len(word2) for _ in range(len(word1))]
        
        for i in range(len(word1)):
            dp[i][0] = i
            
        for j in range(len(word2)):
            dp[0][j] = j
            
        for i in range(1, len(word1)):
            for j in range(1, len(word2)):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    tmp = min(dp[i-1][j], dp[i][j-1])
                    dp[i][j] = min(tmp, dp[i-1][j-1]) + 1
        return dp[-1][-1]
        
        
print("EditDistance DFS: " + str(EditDistanceDFS().compute("abc__xyz_q","abc_hjg_q")))
print("EditDistance DFS CACHE: " + str(EditDistanceDFS_Cache().compute("abc__xyz_q","abc_hjg_q")))
print("EditDistance DP: " + str(EditDistanceDP().compute("abc__xyz_q","abc_hjg_q")))