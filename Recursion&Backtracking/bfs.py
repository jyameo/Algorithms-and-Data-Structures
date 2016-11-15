from string import ascii_lowercase as letters


class WordLadder:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        # write your code here
        queue = [(start, 1)]
        dict.add(end)
        n = len(start)
        while queue:
            cur_word, cur_len = queue.pop(0)
            if cur_word == end:
                return cur_len
            for i in range(n):
                part1, part2 = cur_word[:i], cur_word[i+1:]
                for c in letters:
                    new_word = part1 + c + part2
                    if new_word in dict:
                        queue.append((new_word, cur_len + 1))
                        dict.remove(new_word)

        return 0

    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        # write your code here
        dict.add(start)
        dict.add(end)

        self.parentMap = {}
        for word in dict:
            self.parentMap[word] = []

        cur_level = set()
        cur_level.add(start)

        while True:
            parent_level = cur_level
            cur_level = set()

            for word in parent_level:
                dict.remove(word)

            for word in parent_level:
                for i in range(len(start)):
                    part1, part2 = word[:i], word[i+1:]
                    for c in letters:
                        if c != word[i]:
                            new_word = part1 + c + part2
                            if new_word in dict:
                                self.parentMap[new_word].append(word)
                                cur_level.add(new_word)

            if len(cur_level) == 0:
                return []
            if end in cur_level:
                break

        self.result = []
        self.buildPath([], end)
        return self.result

    def buildPath(self, path, word):
        if len(self.parentMap[word]) == 0:
            self.result.append([word] + path)
            return
        path.insert(0, word)
        for w in self.parentMap[word]:
            self.buildPath(path, w)
        path.pop(0)

start = 'hit'
end = 'cog'
dict = set(['hot', 'dot', 'dog', 'lot', 'log'])
print(WordLadder().ladderLength(start, end, dict))

dict = set(['hot', 'dot', 'dog', 'lot', 'log'])
for words in WordLadder().findLadders(start, end, dict):
    print(words)
