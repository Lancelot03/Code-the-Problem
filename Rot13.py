def rot13(message):
    alpha="abcdefghijklmnopqrstuvwxyz"
    string=''
    for i in message:
        if i in alpha:
            if alpha.index(i)<13:
                string += alpha[alpha.index(i)+13]
            else:
                string += alpha[alpha.index(i)-13]
        elif i in alpha.upper():
            if alpha.upper().index(i)<13:
                string += alpha.upper()[alpha.upper().index(i)+13]
            else:
                string += alpha.upper()[alpha.upper().index(i)-13]
        else:
            string +=i
    return string
