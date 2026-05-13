"""Cho hai chuỗi nhị phân a và b, hãy trả về tổng của chúng dưới dạng một chuỗi nhị phân ."""

class Solution:
    def addBinary(self, a: str, b: str) -> str:

        self.a = a
        self.b = b

        num1 = int(a, 2)
        num2 = int(b, 2)

        total = num1 + num2

        total = format(total, 'b')
        
        return total