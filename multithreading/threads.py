import threading
from time import perf_counter
import time

def function1():
    print('function-1')

def function2():
    print('function-2')

def function3():
    print('function-3')

if __name__ == "__main__":
    t1 = threading.Thread(target=function1)
    t2 = threading.Thread(target=function2)
    t3 = threading.Thread(target=function3)

    time1 = time.perf_counter()

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    time2 = time.perf_counter()

    print(f'Finished in {time2-time1} seconds')