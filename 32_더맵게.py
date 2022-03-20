import heapq

def solution(scoville, K):
    heapq.heapify(scoville)  # heap 자료구조 변경
    cnt = 0  # 섞는 음식 횟수 지정

    while True:
        # 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우 -1 return
        if len(scoville) == 1 and scoville[0] < K:
            return -1

        a = heapq.heappop(scoville)         # 제일 안 매운 음식을 pop 해줌

        if a < K:
            b = heapq.heappop(scoville)     # 2번째로 안 매운 음식 pop 해줌
            new = a + (b * 2)               # 섞은 음식의 스코빌 지수
            heapq.heappush(scoville, new)   # 섞은 음식의 스코빌 지수를 scoville에 넣어줌
            cnt += 1                        # 섞음 음식 카운트
        else:                               # 만약 제일 안 매운 a가 K 이상이면 cnt return
            return cnt