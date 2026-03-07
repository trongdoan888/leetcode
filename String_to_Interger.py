"""Hãy triển khai myAtoi(string s)hàm chuyển đổi chuỗi ký tự thành số nguyên có dấu 32 bit.

Thuật toán myAtoi(string s)được thực hiện như sau:

Khoảng trắng : Bỏ qua bất kỳ khoảng trắng nào ở đầu ( " ").
Tính chất dấu : Xác định dấu bằng cách kiểm tra xem ký tự tiếp theo có phải là '-'hoặc hay không '+', giả định là dương nếu cả hai đều không xuất hiện.
Chuyển đổi : Đọc số nguyên bằng cách bỏ qua các số 0 đứng đầu cho đến khi gặp ký tự không phải chữ số hoặc đến cuối chuỗi. Nếu không đọc được chữ số nào, thì kết quả là 0.
Làm tròn : Nếu số nguyên nằm ngoài phạm vi số nguyên có dấu 32 bit , thì hãy làm tròn số nguyên đó để vẫn nằm trong phạm vi. Cụ thể, các số nguyên nhỏ hơn nên được làm tròn thành , và các số nguyên lớn hơn nên được làm tròn thành .[-231, 231 - 1]-231-231231 - 1231 - 1
Trả về số nguyên làm kết quả cuối cùng.""" 

class Solution:
    def myAtoi(self, s: str) -> int:
        self.s = s 
        s = s.lstrip()
        str_int = ""
       

        for i in range(len(s)):
          
            if i == 0 and (s[i] == "+" or s[i] == "-"):
               str_int += s[i]
               continue
            
            if '0' <= s[i] <= '9':
                str_int += s[i]

            else: break
        
        if str_int == "" or str_int == "+" or str_int == "-":
            return 0
        
        if -2147483648 >= int(str_int): return -2147483648
        elif 2147483647 <= int(str_int): return 2147483647
        return int(str_int)
            

if __name__ == "__main__":
    sol = Solution()

    s = "   -042"
    result = sol.myAtoi(s)

    print(result)