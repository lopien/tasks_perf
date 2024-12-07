n, m = map(int, input().split())

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