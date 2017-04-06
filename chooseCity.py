"""
1보다 큰 N개의 도시 중 한 곳에 공항을 지을 예정입니다.
사람들의 편의를 위해 공항으로부터 각 사람들까지의 도시간 이동 거리가 최소가 되는 도시에 짓기로 하였습니다.
편의상 도시는 일직선상에 놓여있다고 가정하며 좌표의 범위는 음수가 포함됩니다. 또한 좌표는 정렬되어 있지 않습니다.
직선상의 위치와 그 도시에 사는 사람들의 수가 주어질 때,
공항을 지을 도시의 위치를 반환해주는 함수 chooseCity 함수를 완성하세요.
거리가 같은 도시가 2개 이상일 경우 위치가 더 작은 쪽의 도시를 선택하면 됩니다.
예를 들어 다음과 같은 정보의 도시가 있다고 가정해 봅시다.

위치	1	2	3
인구수	5	2	3

이 살 경우, 각각의 도시에 공항을 지었을 때의 사람들의 이동 거리는 8, 8, 12 이므로 1번 또는 2번에 지을 수 있지만,
1의 위치가 더 작으므로 1을 반환해주면 됩니다.
"""
# def chooseCity(n,city):
#     min = 0
#     minnum = 0
#     for i in range(n):
#         m = 0
#         for j in range(n):
#             if i != j:
#                 m += abs(city[j][0]-city[i][0])*city[j][1]
#         if min > m:
#             min = m
#             minnum = i
#     return minnum + 1
# #아래 코드는 출력을 위한 테스트 코드입니다.
#
# print(chooseCity(3,[[1,5],[2,2],[3,3]]))

#미해결

def myFn(s) :
	return s[0]

def chooseCity(n,city):
	answer = 0
	bfrval = 0
	left = [ 0 for x in city]
	leftd = [ 0 for x in city]
	right = [ 0 for x in city]
	rightd = [ 0 for x in city]

	cities = sorted( city, key=myFn )

	for i in range(n) :
		if i == 0 :
			left[i] = 0
			leftd[i] = 0
		else :
			leftd[i] = leftd[i-1] + cities[i-1][1]
			left[i] = left[i-1] + leftd[i]  * ( cities[i][0] - cities[i-1][0] )
		j = n-1-i
		if j == n-1 :
			right[j] = 0
			rightd[j] = 0
		else :
			rightd[j] = rightd[j+1] + cities[j+1][1]
			right[j] = right[j+1] + rightd[j] * ( cities[j+1][0] - cities[j][0] )

	print (left)
	print (right)

	for i in range(n) :
		val = left[i] + right[i]
		if bfrval == 0 :
			bfrval = val
		elif val < bfrval :
			bfrval = val
			answer = i

	return cities[answer][0]
