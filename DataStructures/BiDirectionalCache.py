from time import time

'''
1) 1-1 mapping between keys-values
2) 10k
3) it's a cache
'''


class BiDirectionalCache:
    maxsize = 10000

    def __init__(self):
        self.key_map = dict()
        self.val_map = dict()
        self.count = 0

    def getValue(self, key):
        if key in self.key_map:
            val, t = self.key_map[key]
            self.key_map[key] = [val, time()]
            return val
        else:
            return None

    def put(self, key, value):
        if self.count >= BiDirectionalCache.maxsize:
            self.garbabe_collection()

        t = time()
        self.key_map[key] = [value, t]
        self.val_map[value] = [key, t]
        self.count += 1

    def garbage_collection_(self):
        min_time = self.key_map[0].value()[1]
        min_val = self.key_map[0].value()[0]
        min_key = self.key_map[0].key()
        for key, val in self.key_map.items():
            if val[1] < min_time:
                min_key = key
                min_time = val[1]
                min_val = val[0]
        del self.key_map[min_key]
        del self.val_map[min_val]
        self.count -= 1

    def getKey(self, value):
        if value in self.val_map:
            key, t = self.val_map[value]
            self.val_map[value] = [key, time()]
            return key
        else:
            return None
