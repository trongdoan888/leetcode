"""Cho một chuỗi sgồm các từ và khoảng trắng, hãy trả về độ dài của từ cuối cùng trong chuỗi đó.

Một từ là tối đachuỗi conChỉ bao gồm các ký tự không phải khoảng trắng."""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        self.s = s
        s = s.strip()

        count = 0
        for i in range(len(s) -1, -1 , -1):
            if s[i] == " " :
                break
            if s[i] != " ":
                count += 1
            
        return count
    

# Test case
s = "Hello World"   