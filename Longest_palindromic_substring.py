"""Cho một chuỗi s, hãy trả về chuỗi dài nhất. đối xứng chuỗi conTRONG s."""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s
        
        start, end = 0, 0
        
        def expandAroundCenter(left: int, right: int) -> int:
            """Mở rộng từ tâm để tìm độ dài chuỗi đối xứng dài nhất"""
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1
        
        for i in range(len(s)):
            # Trường hợp 1: Chuỗi đối xứng có độ dài lẻ (tâm là ký tự)
            len1 = expandAroundCenter(i, i)
            # Trường hợp 2: Chuỗi đối xứng có độ dài chẵn (tâm giữa hai ký tự)
            len2 = expandAroundCenter(i, i + 1)
            
            # Lấy độ dài lớn nhất
            max_len = max(len1, len2)
            
            # Cập nhật vị trí bắt đầu và kết thúc nếu tìm được chuỗi dài hơn
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        
        return s[start:end + 1]
    


       
    
    

# if __name__ == "__main__":
#     sol = Solution()
    
#     str1 = "shgugjd"
#     list_char = sol.longestPalindrome(str1)

#     print(list_char)



