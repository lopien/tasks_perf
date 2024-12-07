import sys

n = int(sys.argv[1])
m = int(sys.argv[2])

def task1():
    entry = 1
    path = '1'
    while True:
        entry = (entry + m - 2) % n + 1
        path += str(entry)
        if entry == 1:
            break
    print(path[:-1])
    
task1()

