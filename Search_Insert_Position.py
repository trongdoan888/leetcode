"""Cho một mảng các số nguyên khác nhau đã được sắp xếp và một giá trị cần tìm, hàm này trả về chỉ mục nếu tìm thấy giá trị cần tìm. Nếu không, hãy trả về chỉ mục mà giá trị đó sẽ được chèn vào nếu nó được chèn theo đúng thứ tự.

Bạn phải viết một thuật toán có  O(log n)độ phức tạp thời gian chạy."""

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        self.nums = nums
        self.target = target

        nums.sort()
        
        if target in nums:

            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)
 

if __name__ == "__main__":
    sol = Solution()
    nums = [1,3,5,6]
    target = 2
    x = sol.searchInsert(nums,target)
    print(x)