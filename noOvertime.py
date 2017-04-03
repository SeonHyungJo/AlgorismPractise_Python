"""
야근 지수
회사원인 수민이는 많은 일이 쌓여 있습니다.
수민이는 야근을 최소화하기 위해 남은 일의 작업량을 숫자로 메기고, 일에 대한 야근 지수를 줄이기로 결정했습니다.
야근 지수는 남은 일의 작업량을 제곱하여 더한 값을 의미합니다.
수민이는 1시간 동안 남은 일 중 하나를 골라 작업량 1만큼 처리할 수 있습니다.
수민이의 퇴근까지 남은 N 시간과 각 일에 대한 작업량이 있을 때,
noOvertime 함수를 제작하여 수민이의 야근 지수를 최소화 한 결과를 출력해 주세요.

예를 들어, N=4 일 때,
남은 일의 작업량이 [4, 3, 3] 이라면 야근 지수를 최소화하기 위해 일을 한 결과는 [2, 2, 2]가 되고
야근 지수는 2^2 + 2^2 + 2^2 = 12가 되어 12를 반환해 줍니다.
"""
def noOvertime(n, works):
    for i in range(n):
        m = max(works)
        works.remove(m)
        works.append(m-1)
    return sum(i**2 for i in works)

print(noOvertime(46, [14, 11, 11, 14, 15, 6]))

"""
다른풀이
def noOvertime(n, works):
    if n >= sum(works):
        return 0
    while n > 0:
        works[works.index(max(works))] -= 1
        n -= 1
    result = sum([w ** 2 for w in works])
    # 야근 지수를 최소화 하였을 때의 야근 지수는 몇일까요?
    return result
"""
