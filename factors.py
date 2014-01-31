def coprime(m, n):
    low = min(m, n)
    high = max(m, n)
    for i in range(2, low + 1):
        # print i, low, high, '|', low % i, high % i
        if low % i == 0 and high % i == 0:
            return False
    return True

def inverses(n):
    count = 0
    li = []
    for i in range(2, n):
        if not coprime(n, i):
            continue
        for j in range(2, n):
            #print i, j, n, i * j % n
            if i * j % n == 1:
                count += 1
                li.append(i)
    return count, li

def printout(n, filt=lambda x: x==2):
    for i in range(n):
        count, li = inverses(i)
        if filt(count):
            print i, count, li

printout(100)
