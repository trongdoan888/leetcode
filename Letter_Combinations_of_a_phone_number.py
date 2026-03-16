"""Cho một chuỗi chứa các chữ số từ 2-90 đến 1, hãy trả về tất cả các tổ hợp chữ cái có thể mà số đó có thể đại diện. Trả về kết quả theo bất kỳ thứ tự nào .

Bảng đối chiếu các chữ số với các chữ cái (tương tự như trên các nút điện thoại) được đưa ra bên dưới. Lưu ý rằng số 1 không tương ứng với bất kỳ chữ cái nào."""


class Solution:
    def letterCombinations(self, digits: str):
        phone = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
    
        self.digits = digits
        res = [""]
        for digit in digits:
            new_res = []
            letters = phone[digit]
            for combination in res:
                for char in letters:
                    new_res.append(combination + char)
            res = new_res              
                
        return res
                     
                   


if __name__ == "__main__":
    sol = Solution()

    digits = "237"
    
    x = sol.letterCombinations(digits)
    print(x)
    




