"""Cho một mảng số nguyên numsđược sắp xếp không giảm dần , hãy loại bỏ các phần tử trùng lặp tại chỗ sao cho mỗi phần tử duy nhất chỉ xuất hiện một lần . Thứ tự tương đối của các phần tử phải được giữ nguyên .

Giả sử số lượng phần tử duy nhất trong  numslà . Sau khi loại bỏ các phần tử trùng lặp, hãy trả về số lượng phần tử duy nhất  .k​​​​​​​k

Các phần tử đầu tiên  k của mảng  nums phải chứa các số duy nhất được sắp xếp theo thứ tự . Các phần tử còn lại sau chỉ số này  k - 1 có thể bỏ qua."""

class Solution:
    def removeDuplicates(self, nums: list):
        self.nums = nums

        nums.sort()

        expectedNums = set(nums)

        expectedNums = list(expectedNums)
        return len(expectedNums)

if __name__ == "__main__":
    sol = Solution()
    nums = [1,1,2]
    x = sol.removeDuplicates(nums)
    print(x)
