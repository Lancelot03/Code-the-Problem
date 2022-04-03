import math
import os
import random
import re
import sys
def gradingStudents(grades):
    return [ i if (i < 38 or i % 5 < 3) else (i + (5 - i%5)) for i in grades]
    for i in grades:   
        if i >= 38:
            if i % 5 == 3:
                i += 2
            elif i % 5 == 4:
                i += 1
        return (i)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
