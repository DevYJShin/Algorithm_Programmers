def solution(n, arr1, arr2):
    ans = []
    for i in range(n):
        bin_str = bin(arr1[i] | arr2[i])[2:]
				# [2:]를 하는 이유 - bin( )함수로 인해 0b11111, 여기서 0b는 이진수를 표현하는 문자이므로 제거
        ans.append(("0" *(n - len(bin_str)) + bin_str).replace("1", "#")
                                                      .replace("0", " "))
    return ans