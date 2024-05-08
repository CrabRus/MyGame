import time
import threading
i = 10

def f1(i):
    while True:
        if i <= 0:
            i -= 2
            print(i)
            time.sleep(2)
        else:
            break

def f2(i):
    while True:
        i -= 1
        print(i)
        time.sleep(1)

t1 = threading.Thread(target=f1, args=(i,))
t1.start()