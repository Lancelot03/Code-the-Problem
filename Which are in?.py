def test(st,array):
    for i in array:
        try:
            i.index(st)
            return True
        except ValueError:
            pass
    return False
def in_array(array1, array2):
    return sorted(set(list(filter(lambda x: test(x,array2),array1))))
            
