# Author: Carter Brown

# Given a number A, find the smallest possible value of B+C, if B*C = A.

import math

A = int(input())

factors = []

for i in range(1, int(math.sqrt(A))+1):
    if A%i == 0:
        factors.append([i, int(A/i)])

min_sum = A

for pair in factors:
    min_sum = min(min_sum, pair[0]+pair[1])

print(min_sum)
