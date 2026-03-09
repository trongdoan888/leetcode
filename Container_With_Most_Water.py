"""Cho một mảng số nguyên heightcó độ dài n. Có ncác đường thẳng đứng được vẽ sao cho hai điểm cuối của đường thẳng là và .ith(i, 0)(i, height[i])

Tìm hai đường thẳng cùng với trục x tạo thành một hình trụ, sao cho hình trụ đó chứa được lượng nước nhiều nhất.

Đổ lại lượng nước tối đa mà bình chứa có thể chứa được .

Lưu ý rằng bạn không được nghiêng hộp đựng."""

class Solution:
    def maxArea(self, height) -> int:
        self.height = height
        max = 0

        for i in range(len(height) - 1):
            for j in range(1,len(height)): 
                if height[i] >= height[j]:
                    s = height[j] * (j - i) 
                else:
                    s = height[i] * (j - i)

                if s > max:
                    max = s
        
        return max
    
class Solution:
    def maxArea(self, height):
        i = 0
        j = len(height) - 1
        res = 0

        while i < j:
            res = max(res, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return res
    
class Solution:
    def maxArea(self, height) -> int:
        max_area = 0
        l = 0
        r = len(height)-1
        max_height = max(height)

        while l < r:
            height_l, height_r = height[l], height[r]

            if height_l < height_r:
                curr_area = (r-l) * height_l
                l += 1
            else:
                curr_area = (r-l) * height_r
                r -= 1
            max_area = max(max_area, curr_area)

            if max_height * (r-l) < max_area: # Check potential max_area
                break

        return max_area

        


if __name__ == "__main__":
    sol = Solution()

    height = [1,2]

    max = sol.maxArea(height)

    print(max)



