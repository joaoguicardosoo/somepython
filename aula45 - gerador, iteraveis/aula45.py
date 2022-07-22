import sys
import time

def gera():
    r = []
    for n in range(100):
        r.append(n)
        time.sleep(0.1)
    return r

print(gera())