from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 수평선 검사
        for i in range(9):
            cur = board[i]
            num_check = [False for _ in range(10)]

            for j in range(9):
                if cur[j] == '.':
                    continue

                if num_check[int(cur[j])]:
                    return False
                num_check[int(cur[j])] = True

        # 수직선 검사
        for i in range(9):
            num_check = [False for _ in range(10)]

            for j in range(9):
                if board[j][i] == '.':
                    continue

                if num_check[int(board[j][i])]:
                    return False
                num_check[int(board[j][i])] = True

        # 3*3 검사
        for i in range(3):
            for j in range(3):
                num_check = [False for _ in range(10)]

                for k in range(3*i, 3*i + 3):
                    for l in range(3*j, 3*j + 3):
                        if board[k][l] == '.':
                            continue

                        if num_check[int(board[k][l])]:
                            return False
                        num_check[int(board[k][l])] = True

        return True


def test_case():
    solution = Solution()

    ex_1 = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    assert solution.isValidSudoku(ex_1) == True

    ex_2 = [["8", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    assert solution.isValidSudoku(ex_2) == False
