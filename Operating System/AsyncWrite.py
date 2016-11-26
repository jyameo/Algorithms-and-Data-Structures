from threading import Thread, Lock
from time import sleep, time

class AsyncWrite(Thread):
    def __init__(self, text, out):
        Thread.__init__(self)
        self.text = text
        self.out = out
        
    def run(self):
        print("Started Background File Write to " + self.out)
        f = open(self.out, "a")
        f.write(self.text+ '\n')
        f.close()
        sleep(2)
        print("Finished Background File Write to " + self.out)
        
def main():
    msg = input("Enter text to save: ->")
    background = AsyncWrite(msg, 'out.txt')
    background.start()
    print("Main thread still alive!")
    
    background.join()
    print("Main thread waited until background completes")

if __name__ == '__main__':
    main()