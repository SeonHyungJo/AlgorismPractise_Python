"""
어떤 수를 입력받아 그 수의 약수를 모두 더한 수 sumDivisor 함수를 완성해 보세요.
 예를 들어 12가 입력된다면 12의 약수는 [1, 2, 3, 4, 6, 12]가 되고, 총 합은 28이 되므로 28을 반환해 주면 됩니다.
"""
def sumDivisor(num):
    answer = 0
    for i in range(1,num+1):
        if num%i == 0:
            answer += i
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(sumDivisor(12))


"""
다른풀이
def sumDivisor(num):
    # num / 2 의 수들만 검사하면 성능 약 2배 향상잼
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])
"""
