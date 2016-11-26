from multiprocessing import Pool
from time import time


def f(n):
    sum = 0
    for x in range(1000):
        sum += x*x
    return sum
    
def main():
    numb = 10000
    t1 = time()
    p = Pool(processes=2)
    result = p.map(f, range(numb))
    p.close()
    p.join()
    
    print("Pool took: ", time() - t1)
    
    t2 = time()
    res = []
    for x in range(numb):
        res.append(f(x))
        
    print("Serial processing took: ", time() - t2)
if __name__ == '__main__':
    main()