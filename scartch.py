import math
import os
import random
import re
import sys


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    count = 0
    emma_pos = 0
    d = c
    d.append(1)
    d.append(1)
    while emma_pos < (len(c)):
        if d[emma_pos + 1] == 0:
            if d[emma_pos + 2] == 0:
                emma_pos = emma_pos + 2
                count += 1
            else:
                emma_pos = emma_pos + 1
                count += 1
        elif d[emma_pos + 2] == 0:
            emma_pos = emma_pos + 2
            count += 1

    return count


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)