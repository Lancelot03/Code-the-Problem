if __name__ == '__main__':
    import sys
    n, k = map(int, sys.stdin.readline().strip().split())
    t = list(map(int, sys.stdin.readline().strip().split()))
    page = 0
    n_special = 0
    for i in range(n):
        page += 1
        for j in range(1, t[i] + 1):
            if j == page:
                n_special += 1
            if j != 0 and j % k == 0 and j < t[i]:
                page += 1
    print(n_special)
