from multiprocessing import Process, Array, Queue
from time import time, sleep


def calc_square(numbers, shared_result, shared_q):
    for idx, n in enumerate(numbers):
        sleep(0.5)
        print('Square ' + str(n*n))
        shared_result[idx] = n*n
        shared_q.put(n*n)
    print("Inside square: Shared Result => " + str(shared_result[:]))
        
def calc_cube(numbers, shared_result, shared_q):
    for idx, n in enumerate(numbers):
        sleep(0.5)
        print('Cube ' + str(n*n*n))
        shared_result[idx+4] = n*n*n
        shared_q.put(n*n*n)
    print("Inside cube: Shared Result => " + str(shared_result[:]))

def main():
    arr = [2,3,8,9]
    
    shared_result = Array('i', 8)
    #shared_value = Value('d', 0.0)
    shared_q = Queue()
    p1 = Process(target=calc_square, args=(arr, shared_result, shared_q))
    p2 = Process(target=calc_cube, args=(arr, shared_result, shared_q))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    print('Global Shared Result => ' + str(shared_result[:]))
    
    print('Global Shared Queue')
    while not shared_q.empty():
        print(shared_q.get())
    print("Main thread completed.")

if __name__ == '__main__':
    main()