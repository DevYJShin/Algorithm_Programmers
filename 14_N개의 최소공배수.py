import math

def solution(num):
    answer = num[0]
    for n in num:
        answer = (n * answer) // math.gcd(n, answer)
    return answer