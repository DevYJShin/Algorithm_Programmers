def solution(answers):
    answer = []
    # 패턴정의
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    # 점수정의
    first_count = 0
    second_count = 0
    third_count = 0

    # 정답확인
    for number in range(len(answers)):
        if answers[number] == first[number % 5]:
            first_count += 1
        if answers[number] == second[number % 8]:
            second_count += 1
        if answers[number] == third[number % 10]:
            third_count += 1
    pre_answer = [first_count, second_count, third_count]

    # 가장 많이 맞힌 사람
    for person, score in enumerate(pre_answer):
        if score == max(pre_answer):
            answer.append(person + 1)
    return answer