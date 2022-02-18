def solution(phone_book):
    # Hash map을 만든다.
    hash_map = {}
    for number in phone_book:
        hash_map[number] = 1

        print(hash_map)


# 2. 접두어가 Hash map에 존재하는지 찾는다.
for phone_number in phone_book:
    jubdoo = ''
    for number in phone_number:
        jubdoo += number

        # 3. 접두어를 찾아야 한다. (기존 번호와 같은 경우는 제외한다.)
        if jubdoo in hash_map and jubdoo != phone_number:
            return False
return True

print(solution(["6", "12", "6789"]))