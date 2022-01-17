import math

def solution(progresses, speeds):
    n = len(progresses)
    date_left = []
    answer = []

    for i in range(n):
        progress_left = 100 - progresses[i]
        share = math.ceil(progress_left / speeds[i])
        date_left.append(share)

    while date_left:
        left = date_left.pop(0)
        result = 1
        while len(date_left) != 0 and left >= date_left[0]:
            result += 1
            date_left.pop(0)
        answer.append(result)

    return answer