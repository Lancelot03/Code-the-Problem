def square_sum(numbers):
    a=[]
    for i in range(len(numbers)):
        a.append(numbers[i]**2)
    return sum(a)
