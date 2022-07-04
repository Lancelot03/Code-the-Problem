def duplicate_count(text):
    if len(text) == 0:
        return 0
    text=text.lower()
    count=0
    for i in set(text):
        if text.count(i)>1:
            count +=1
    return count
