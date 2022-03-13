# 배열을 활용한 Solution

# reserve 1 3 5
# lost 24
# student 0  1  2  3  4  5  6
#         0  1 -1  1 -1  1  0

# -1 -> 체육복이 없음
#  0 -> 체육복을 가지고 있음
#  1 -> 체육복을 가지고 있음 + 체육복 여분이 있음

def solution(n, lost, reserve):     # 함수 매개변수 n=학생수, lost= 체육복 없음, reserve= 체육복 여분 있음
    # 1. student 배열 생성
    student = [0] * (n+2)           # n+2인 이유 - 1앞 0과 5 뒤 6의 값은 0으로 없는 값이지만 추가

    # 2. reserve/lost 정보 반영
    for r in reserve:               # r번 학생은 1 증가
        student[r] += 1             # r번 학생은 여분이 있기 때문에 빌려줄 수 있다.
    for l in lost:                  # l번 학생은 1 감소
        student[l] -= 1             # l번 학생은 체육복이 없기 때문에 필요하다.

    # 3. 여분을 기준으로 앞뒤를 확인하여 체육복을 빌려준다.
    for i in range(1, n+1):         # n번을 포함하는 값까지 반복
        if student[i] > 0:          # 학생이 체육복 여분이 있는지 조건 확인
            front = i - 1
            back = i + 1

            if student[front] < 0:  # 내 앞에 있는 학생이 체육복이 필요하다면
                student[i] -= 1     # 본인 체육복 여분 하나를 뺀다.
                student[front] += 1 # 앞에 있는 학생은 체육복이 빌린다.
            elif student[back] < 0: # 내 뒤에 있는 학생이 체육복이 필요하다면
                student[i] -= 1     # 본인 체육복 여분 하나를 뺀다.
                student[back] += 1  # 뒤에 있는 학생은 체육복을 빌린다.

    # 4. 체육복을 갖고 있는 학생 수를 계산한다.
    answer = 0                      # 체육복을 갖고 있는지 확인할 변수 초기화
    for i in range(1, n+1):         # 다시 1부터 n까지 반복
        if student[i] >= 0:         # 학생들이 체육복을 가지고 있다면
            answer += 1             # 1 증가
    return answer
