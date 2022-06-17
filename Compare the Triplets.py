def compareTriplets(a, b):
    alice = [1 for (al, bob) in zip(a, b) if al > bob]
    bob = [1 for (al, bo) in zip(a, b) if bo > al]
    return [sum(alice), sum(bob)]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
