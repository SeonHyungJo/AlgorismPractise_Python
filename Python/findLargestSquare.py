"""
O와 X로 채워진 표가 있습니다. 표 1칸은 1 x 1 의 정사각형으로 이루어져 있습니다.
표에서 O로 이루어진 가장 큰 정사각형을 찾아 넓이를 반환하는 findLargestSquare 함수를 완성하세요.
예를 들어

1	2	3	4	5
X	O	O	O	X
X	O	O	O	O
X	X	O	O	O
X	X	O	O	O
X	X	X	X	X
가 있다면 정답은

1	2	3	4	5
X	O	O	O	X
X	O	O	O	O
X	X	O	O	O
X	X	O	O	O
X	X	X	X	X
가 되며 넓이는 9가 되므로 9를 반환해 주면 됩니다.
"""
#미해결

def findLargestSquare(board):
    answer = 0
    n = 0
    max = 0
    count2 = 0
    for i in range(len(board)):
        count = 0
        for j in range(len(board[i])):
            if board[i][j] == 'O':
                print("count : ", count)
            elif board[i][j] == 'X':
                for k in range(1u, count):
                    if board[k][j]=='O':
                        print("pass실행")
                        count2 += 1
                        if count == count2:
                            answer = count ** count2
                            print(answer)
                        pass
                    else:
                        print("break실행")
                        print(count)
                        break
                print("finish break")
            else:
                break

            print(board[i][j])




    # for i in range(len(board)):
    #     if board[n][i] == 'O':
    #         for j in range(i, len(board)):
    #             if board[n][j] == 'O':
    #                 print(board[n][j])
    #                 count += 1
    #                 print(count)
    return answer

#아래 코드는 출력을 위한 테스트 코드입니다.

testBoard = [['O','O','X'],['O','O','O']]
print(findLargestSquare(testBoard))
