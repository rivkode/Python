board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
bsk = []
cnt = 0

for i in moves:
    if board[i - 1][-1] != 0:
        if bsk[-1] != board[i - 1][-1]:
            bsk.append(board[i - 1][-1])
            board.pop([i - 1][-1])
        else:
            bsk.pop()
            cnt += 2
    else:
        continue


answer = cnt
