"""
두 수의 최소공배수(Least Common Multiple)란 입력된 두 수의 배수 중 공통이 되는 가장 작은 숫자를 의미합니다.
예를 들어 2와 7의 최소공배수는 14가 됩니다. 정의를 확장해서,
n개의 수의 최소공배수는 n 개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됩니다.
nlcm 함수를 통해 n개의 숫자가 입력되었을 때, 최소공배수를 반환해 주세요.
예를들어 [2,6,8,14] 가 입력된다면 168을 반환해 주면 됩니다.
"""
#미해결
def gcd(a, b, num):
    while b:
        a, b = b, a % b
    if a != 0 or a != 1:
        n1 = []
        for i in range(len(num)):
            if num[i] % a == 0:
                n1.append((int)(num[i]//a))
            else:
                n1.append(num[i])
        return n1, a
    return num, 1

def nlcm(num):
    n1 = 1
    answer = 1
    for i in range(len(num)):
        for j in range(i+1, len(num)):
            if(num[i] != 0 and num[j] != 0):
                tuple = gcd(num[i], num[j], num)
                num = tuple[0]
                n1 = tuple[1]*n1
    for i in num:
        answer *= i
    return answer*n1



# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(nlcm([84, 71, 76, 59, 63, 12, 62, 66, 18, 26]));
