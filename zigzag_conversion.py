"""Chuỗi ký tự "PAYPALISHIRING"được viết theo kiểu zigzag trên một số hàng nhất định như thế này: (bạn có thể muốn hiển thị mẫu này bằng một phông chữ cố định để dễ đọc hơn)"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        self.s = s 
        self.numRows = numRows 
        
        str_result = ""
        count = len(s) 
        arr = [[0 for _ in range(numRows)] for _ in range(len(s))]
        numRows = numRows - 1

        def ping_pong(x,n):
            if n == 0:
                return 0
                
            t = x % (2 * n)
            return t if t <= n else 2 * n - t

        for i in range(len(s)):
            t = ping_pong(i, numRows)    
            arr[i][t] = s[i]
         
             
        for i in range(numRows + 1):
            for j in range(len(s)):
                if arr[j][i] != 0:
                    str_result += arr[j][i]

        
        return str_result


sol = Solution()

s = "S"
numRows = 1

list_result = sol.convert(s,numRows)
                 
print(list_result)
                