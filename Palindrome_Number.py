"""Cho một số nguyên x, trả về giá trị truenếu xlà một số nguyênxuôi ngược đều giống nhauvà falsengược lại ."""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        self.x = x
        check = True

        if x < 0:
            return False
        elif x >= 0:
            y = str(x)
            y = y[::-1]
            y  = int(y)

        if x == y:
            check = True
        else:
            check = False
        
        return check
    

if __name__ == "__main__":
    sol = Solution()
    x = 10

    check = sol.isPalindrome(x)

    print(check)
