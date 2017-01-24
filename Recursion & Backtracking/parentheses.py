class ParenthesesDFS(object):
    def generate(self, n):
        if n < 1:
            return []
        elif n == 1:
            return ["()"]
            
        self.result = []
        
        def dfs(l, r, current):
            if l == n and r == n:
                self.result.append(current)
                return
            
            if l < n:
                dfs(l+1, r, current + "(")
            if r < l:
                dfs(l, r+1, current + ")")
            
        dfs(0, 0, "")
        return self.result
        

class Node(object):
    def __init__(self, l, r, current):
        self.l = l
        self.r = r
        self.current = current
        
class ParenthesesBFS(object):
    def generate(self, n):
        q = []
        result = []
        
        if n < 1:
            return result
        if n == 1:
            return ["()"]
        
        q.append(Node(0,0,""))
        
        while q:
            cur = q.pop(0)
            
            if cur.l == n and cur.r == n:
                result.append(cur.current)
            else:
                if cur.l < n:
                    q.append(Node(cur.l+1, cur.r, cur.current + "("))
                
                if cur.r < cur.l:
                    q.append(Node(cur.l, cur.r+1, cur.current + ")"))
        return result
        
class Parentheses_NON_REC_DFS(object):
    def generate(self, n):
        s = []
        result = []
        
        if n < 1:
            return result
        if n == 1:
            return ["()"]
        
        s.append(Node(0,0,""))
        
        while s:
            cur = s.pop()
            
            if cur.l == n and cur.r == n:
                result.append(cur.current)
            else:
                if cur.l < n:
                    s.append(Node(cur.l+1, cur.r, cur.current + "("))
                
                if cur.r < cur.l:
                    s.append(Node(cur.l, cur.r+1, cur.current + ")"))
        return result
        

print("Parentheses DFS: " + str(ParenthesesDFS().generate(3)))
print("Parentheses BFS: " + str(ParenthesesBFS().generate(3)))
print("Parentheses NON REC DFS: " + str(Parentheses_NON_REC_DFS().generate(3)))