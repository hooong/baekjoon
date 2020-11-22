from collections import deque

def solution(board, moves):
    answer = 0
    board_stack = [deque() for _ in range(len(board))]
    bucket = deque()
    
    for row in board[::-1]:
        for i in range(len(row)):
            if not row[i] == 0:
                board_stack[i].append(row[i])
    
    for num in moves:
        if board_stack[num-1]:
            doll = board_stack[num-1].pop()
        
            if bucket:
                if doll == bucket[-1]:
                    bucket.pop()
                    answer += 2
                else:
                    bucket.append(doll)
            else:
                bucket.append(doll)
    
    return answer