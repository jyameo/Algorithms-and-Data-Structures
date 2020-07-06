class TrieNode:
    def __init__(self,label=None,data=None):
        self.label = label
        self.data = data
        self.children = {}
        
class TrieTree:
    def __init__(self):
        self.root = TrieNode()
        
    def add(self, word):
        if not word:
            return 
        
        current = self.root
        for i in range(len(word)):
            if word[i] in current.children:
                current = current.children[word[i]]
            else:
                break
                
        while i < len(word):
            current.children[word[i]] = TrieNode(word[i])
            current = current.children[word[i]]
            i += 1
        
        current.data = word
        
    
    def has_prefix(self, prefix):
        if not self.root:
            return []
        
        current = self.root
        for i in range(len(prefix)):
            if prefix[i] in current.children:
                current = current.children[prefix[i]]
            else:
                return []
            
        q = []
        q = [current]
            
        words = []
        while q:
            node = q.pop(0)
            if node.data != None:
                words.append(node.data)
            
            for child in node.children.values():
                q.append(child)
        return words


words = ["abc", "acd", "bcd", "def", "a", "aba"]
t = TrieTree()
for word in words:
    t.add(word)

t.has_prefix('a')
