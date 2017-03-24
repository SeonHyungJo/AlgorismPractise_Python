"""
strange_sort함수는 strings와 n이라는 매개변수를 받아들입니다.
strings는 문자열로 구성된 리스트인데, 각 문자열을 인덱스 n인 글자를 기준으로 정렬하면 됩니다.

예를들어 strings가 ["sun", "bed", "car"]이고 n이 1이면 각 단어의 인덱스 1인 문자 u, e ,a를 기준으로 정렬해야 하므로 결과는 ["car", "bed", "sun"]이 됩니다.
strange_sort함수를 완성해 보세요.
"""
def strange_sort(strings, n):
    '''strings의 문자열들을 n번째 글자를 기준으로 정렬해서 return하세요'''
    a = []
    b = []

    for i in range(len(strings)):
        a.append([(strings[i])[n], strings[i]])

    for i in range(len(strings)):
        b.append((sorted(a))[i][1])

    return b
# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( strange_sort(["sun", "bed", "car"], 1) )

"""
다른풀이
def strange_sort(strings, n):
    '''strings의 문자열들을 n번째 글자를 기준으로 정렬해서 return하세요'''
    return sorted(strings, key=lambda x: x[n])

strings = ["sun", "bed", "car"]
print(strange_sort(strings, 1))
"""
