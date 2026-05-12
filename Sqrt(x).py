"""Cho một số nguyên không âm x, hãy trả về căn bậc hai của số đó x, làm tròn xuống số nguyên gần nhất . Số nguyên trả về cũng phải là số không âm .

Bạn không được sử dụng bất kỳ hàm hoặc toán tử lũy thừa tích hợp nào.

Ví dụ, không nên sử dụng pow(x, 0.5)trong C++ hoặc x ** 0.5Python."""

class Solution:
    def mySqrt(self, x: int) -> int:
        self.x = x

        if x < 2:
            return x
        
        left = 1
        right = x // 2
        ans = 0

        while left <= right:
            mid = (left + right) // 2

            if mid * mid == x:
                return mid
            
            elif mid * mid < x:
                left = mid + 1
                ans = mid
            else:
                right = mid - 1 
        

        return ans