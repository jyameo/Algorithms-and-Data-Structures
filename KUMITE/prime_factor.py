
class Prime(object):
    def __init__(self):
        self.factors = dict()
    
    def primeFactors(self, n):
        for y in range(2, n+1):
            if n%y == 0:
                if y in self.factors:
                    self.factors[y] +=1
                else:
                    self.factors[y] = 1
                self.primeFactors(n//y)
                break

        
p = Prime()
p.primeFactors(24)
print(p.factors)
    