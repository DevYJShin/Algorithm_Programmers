def solution(participant, completion):
    hash_dict = {}
    sum_hash = 0

    # hash - key, value pair라는게 존재하고, 딕셔너리라는 자료구조
    # [hash(part)] - key / part - value

    # 1. participant list의 hash를 구하고, hash 값을 더한다.
    for part in participant:
        hash_dict[hash(part)] = part
        sum_hash += hash(part)

    # 2. completion list의 hash를 빼준다.
    for comp in completion:
        sum_hash -= hash(comp)

    # 3. 남은 값이 완주하지 못한 선수의 hash 값이 된다.
    return hash_dict[sum_hash]


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))