"""Hãy viết chương trình giải câu đố Sudoku bằng cách điền vào các ô trống.

Lời giải Sudoku phải thỏa mãn tất cả các quy tắc sau :

Mỗi chữ số 1-9phải xuất hiện chính xác một lần trong mỗi hàng.
Mỗi chữ số 1-9phải xuất hiện chính xác một lần trong mỗi cột.
Mỗi chữ số 1-9phải xuất hiện chính xác một lần trong mỗi ô nhỏ trong số 9 3x3ô của lưới.
Ký tự này '.'biểu thị các ô trống."""


class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Mảng đánh dấu: Kiểm tra xem số (1-9) đã xuất hiện ở đâu chưa
        # Mảng 9x10 (bỏ qua cột 0 cho dễ dùng index từ 1 đến 9)
        rows = [[False] * 10 for _ in range(9)]
        cols = [[False] * 10 for _ in range(9)]
        boxes = [[False] * 10 for _ in range(9)]
         n 
        empty_cells = []
        
        # BƯỚC 1: Quét bảng 1 lần duy nhất để khởi tạo dữ liệu
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empty_cells.append((r, c)) # Lưu tọa độ ô trống
                else:
                    num = int(board[r][c])
                    box_idx = (r // 3) * 3 + (c // 3)
                    
                    # Đánh dấu số `num` đã tồn tại
                    rows[r][num] = True
                    cols[c][num] = True
                    boxes[box_idx][num] = True

        # BƯỚC 2: Viết hàm Quay lui duyệt trên danh sách ô trống
        def backtrack(idx: int) -> bool:
            # Nếu đã điền xong tất cả ô trống -> Thành công!
            if idx == len(empty_cells):
                return True
            
            # Lấy tọa độ ô trống hiện tại
            r, c = empty_cells[idx]
            box_idx = (r // 3) * 3 + (c // 3)
            
            # Thử các số từ 1 đến 9
            for num in range(1, 10):
                # O(1) Kiểm tra cực nhanh xem số này đã dùng chưa
                if not rows[r][num] and not cols[c][num] and not boxes[box_idx][num]:
                    
                    # ĐIỀN THỬ
                    board[r][c] = str(num)
                    rows[r][num] = cols[c][num] = boxes[box_idx][num] = True
                    
                    # Đi tới ô trống tiếp theo (idx + 1)
                    if backtrack(idx + 1):
                        return True
                        
                    # BACKTRACK: Xóa số, bỏ đánh dấu
                    board[r][c] = "."
                    rows[r][num] = cols[c][num] = boxes[box_idx][num] = False
                    
            return False # Không số nào hợp lệ -> Lùi lại

        # BƯỚC 3: Bắt đầu thuật toán từ ô trống đầu tiên (index 0)
        backtrack(0)