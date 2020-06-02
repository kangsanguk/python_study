def solution(board, moves):
    answer = 0
    stack = []
    for i in moves:
        k = 0
        while (k < len(board)):
            if board[k][i-1] != 0:
                if len(stack) == 0:
                    stack.append(board[k][i-1])
                elif stack[-1] != board[k][i-1]:
                    stack.append(board[k][i-1])
                else:
                    del stack[-1]
                    answer += 2
                board[k][i-1] = 0
                break
            k += 1
    return answer
