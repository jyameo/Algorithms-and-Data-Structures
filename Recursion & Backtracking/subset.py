class Subset_dfs(object):
    def compute(self, S):
        self.result = []
        
        if not S or len(S) == 0:
            return self.result
        
        def dfs(pos, current):
            if pos == len(S):
                self.result.append(list(current))
                return
            
            dfs(pos+1, current)
            current.append(S[pos])
            dfs(pos+1, current)
            current.pop()
        
        dfs(0, [])
        return self.result
    
class Node(object):
    def __init__(self, idx):
        self.index = idx
        self.current = []
        
class Subset_bfs(object):
    def compute(self, S):
        q = []
        result = []
        q.append(Node(0))
        
        while q:
            n = q.pop(0)
            
            if n.index == len(S):
                result.append(n.current)
            else:
                n1 = Node(n.index + 1)
                n1.current = list(n.current)
                n1.current.append(S[n.index])
                
                n.index += 1
                
                q.append(n)
                q.append(n1)
                
        return result
        
class Subset_non_rec_dfs(object):
    def compute(self, S):
        s = []
        result = []
        s.append(Node(0))
        
        while s:
            n = s.pop()
            
            if n.index == len(S):
                result.append(n.current)
            else:
                n1 = Node(n.index + 1)
                n1.current = list(n.current)
                n1.current.append(S[n.index])
                
                n.index += 1
                
                s.append(n)
                s.append(n1)
                
        return result
        
print('Subset DFS: ' + str(Subset_dfs().compute([1, 2, 3])))
print('Subset BFS: ' + str(Subset_bfs().compute([1, 2, 3])))
print('Subset NON REC DFS: ' + str(Subset_non_rec_dfs().compute([1, 2, 3])))