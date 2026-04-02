"""Mỗi hàng phải chứa các chữ số  1-9mà không được lặp lại.
Mỗi cột phải chứa các chữ số  1-9 mà không được lặp lại.
Mỗi trong chín  3 x 3ô nhỏ của lưới phải chứa các chữ số  1-9 mà không được lặp lại."""


class Solution:
    def isValidSudoku(self, board: list) -> bool:
        
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):

                val = board[r][c]
                if val == ".":
                    continue

                box_idx = (r // 3) * 3 + (c // 3)

                if val in rows[r] or val in cols[c] or val in boxes[box_idx]:
                    return False
                
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_idx].add(val)
        

        return True