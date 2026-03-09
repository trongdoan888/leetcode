"""Cho một số nguyên 32 bit có dấu x, hãy trả x về giá trị đã đảo ngược các chữ số .
 Nếu việc đảo ngược xkhiến giá trị nằm ngoài phạm vi số nguyên 32 bit có dấu , 
 thì hãy trả về giá trị rỗng .[-231, 231 - 1]0"""

class Solution:
    def reverse(self, x: int) -> int:   
        self.x = x
        y = 0
        if 2**31 - 1 > x >= 0:
            x_str = str(x)
            x_str = x_str[::-1]
            y = int(x_str)
        elif 0 > x > -2**31:
            x = x * -1
            x_str = str(x)
            x_str = x_str[::-1]
            y = int(x_str) * -1   
        elif  x < -2**31 or x > 2**31 - 1:
            y = 0
        
        if y < -2**31 or y > 2**31 - 1:
            y = 0 
        return y
    
    def reverse(self, x: int) -> int:   
        self.x = x 

        y = str(x)
        if y[0] == "+" or y[0] == "-":
            res = int(y[0] + y[1:][::-1] )
        else : res = int(y[::-1])
        
        if -2147483648 >= res or res >= 2147483647: return 0
        return res

if __name__ == "__main__":

    sol = Solution()

    x = 1534236469
    y = sol.reverse(x)

    print(y)

