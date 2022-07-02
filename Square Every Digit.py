def square_digits(num):
    r = ''
    for l in str(num):
        r = r + str((int(l))**2)
    return int(r)
