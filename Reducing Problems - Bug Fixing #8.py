def calculate_total(t1, t2):
    if sum(t1) ==0:
        return False
    if sum(t2)== 0:
        return True
    if sum(t1)> sum(t2):
        return True
    else:
        return False
    if sum(t1) == 0 and sum(t2)==0:
        return False
