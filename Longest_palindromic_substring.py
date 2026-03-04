"""Cho một chuỗi s, hãy trả về chuỗi dài nhất. đối xứng chuỗi conTRONG s."""

# class Solution:
def manacher_simulation(s):
    # Bước 1: Chuẩn bị chuỗi t (Dùng t để tính toán thay vì s)
    t = "^#" + "#".join(s) + "#$"
    n = len(t)          # n phải là độ dài của chuỗi t
    p = [0] * n        # p phải cùng độ dài với t
    c = 0
    r = 0

    print("Chuỗi đã qua xử lý :", t)

    # Bước 2: Duyệt qua từng tâm i
    for i in range(1, n - 1): # Chạy từ 1 đến n-2 để tránh ký tự ^ và $
        if i < r:
            mirror = 2 * c - i
            p[i] = min(r - i, p[mirror])
            status = "Mượn dữ liệu"
        else:
            p[i] = 0
            status = "Quét mới hoàn toàn"

        # --- ĐÂY LÀ PHẦN BẠN CÒN THIẾU: Mở rộng thêm ---
        while t[i + 1 + p[i]] == t[i - 1 - p[i]]:
            p[i] += 1
            status = "Đang mở rộng thêm..."

        # Bước 3: Cập nhật tâm và biên mới
        if i + p[i] > r:
            c = i
            r = i + p[i]

        char_display = t[i]
        print(f"Tâm {i:2} ('{char_display}'): Bán kính = {p[i]} | {status}")

    # Bước 4: Trích xuất kết quả
    max_len = max(p)
    center_index = p.index(max_len)
    
    # Công thức chuẩn để lấy lại chuỗi gốc từ chuỗi t
    start = (center_index - max_len) // 2
    result = s[start : start + max_len]

    return result

original_string = "ababa"
print(f"Chuỗi gốc: {original_string}")
final_result = manacher_simulation(original_string)
print("-" * 50)
print(f"Kết quả cuối cùng: {final_result}")
    


       
    
    

# if __name__ == "__main__":
#     sol = Solution()
    
#     str1 = "shgugjd"
#     list_char = sol.longestPalindrome(str1)

#     print(list_char)



