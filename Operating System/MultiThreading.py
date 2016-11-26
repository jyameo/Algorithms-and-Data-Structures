from threading import Thread
from time import sleep, time, ctime


def timer(name, delay, repeat):
    print("Timer: " + name + " started")
    while repeat > 0:
        sleep(delay)
        print(name + ": " + str(ctime(time())))
        repeat -= 1
    print("Timer: " + name + " completed")
    
    
def main():
    t1 = Thread(target=timer, args=("Timer1", 1, 5))
    t2 = Thread(target=timer, args=("Timer2", 2, 5))
    
    t1.start()
    t2.start()
    
    print("Main thread completed")

if __name__ == '__main__':
    main()