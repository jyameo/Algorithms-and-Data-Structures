from threading import Thread, Lock
from time import sleep, time, ctime

tLock = Lock()

def timer(name, delay, repeat):
    print("Timer: " + name + " started")
    
    # CRITICAL SECTION
    tLock.acquire()
    print(name + " has acquired the lock!")
    while repeat > 0:
        sleep(delay)
        print(name + ": " + str(ctime(time())))
        repeat -= 1
    print(name + " is releasing the lock!")
    tLock.release()
    
    print("Timer: " + name + " completed")
    
    
def main():
    t1 = Thread(target=timer, args=("Timer1", 1, 5))
    t2 = Thread(target=timer, args=("Timer2", 2, 5))
    
    t1.start()
    t2.start()
    
    print("Main thread completed")

if __name__ == '__main__':
    main()