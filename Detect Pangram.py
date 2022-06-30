import string
def is_pangram(s):
    if len(set('abcdefghijklmnopqrstuvwxyz') - set(s.lower())) == 0 :
        return True

    return False

user_str = "The quick brown fox jumps over the lazy dog"

if(is_pangram(user_str)):
    print("It is a pangram string")
else:
    print("Not a pangram string")
