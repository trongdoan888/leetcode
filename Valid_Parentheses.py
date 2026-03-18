"""Cho một chuỗi schỉ chứa các ký tự '(', ')', '{', '}', '['và ']', hãy xác định xem chuỗi đầu vào có hợp lệ hay không.

Chuỗi đầu vào được coi là hợp lệ nếu:

Dấu ngoặc mở phải được đóng bằng cùng loại dấu ngoặc.
Các dấu ngoặc mở phải được đóng theo đúng thứ tự.
Mỗi dấu ngoặc đóng đều có một dấu ngoặc mở tương ứng cùng loại."""

class Solution:
    def isValid(self, s: str) -> bool:
        self.s = s
        mapping = {
        ')': '(',
        '}': '{',
        ']': '['
        }

        stack = []

        for char in s:
            if char in mapping:  # nếu là ngoặc đóng
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:  # ngoặc mở
                stack.append(char)
    
        return len(stack) == 0