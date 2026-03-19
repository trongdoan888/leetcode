"""Cho một mảng số nguyên numsvà một số nguyên val, hãy xóa tất cả các lần xuất hiện của valtrong mảng nums tại chỗ . Thứ tự của các phần tử có thể được thay đổi. Sau đó, trả về số lượng phần tử trong numsmảng mà không bằngval .

Hãy xem xét số lượng phần tử numskhông bằng là val, kđể được chấp nhận, bạn cần thực hiện những điều sau:

Hãy thay đổi mảng numssao cho kcác phần tử đầu tiên của numschứa các phần tử không bằng val. Các phần tử còn lại của numskhông quan trọng, cũng như kích thước của nums.
Trở lại k."""

class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        self.nums = nums
        self.val = val
        left = 0
        right = len(nums) - 1
        index = []

        if len(nums) == 1:
            if nums[0] == val:
                return 0
            else: 
                return 1
        
        while left <= right:
            if left == right:
                if nums[left] == val:
                    index.append(left)

            if nums[left] == val :
                index.append(left)
            if nums[right] == val:
                index.append(right)
            left += 1
            right -= 1
        
        for i in sorted(index, reverse=True):
            nums.pop(i)

        
        return len(nums) 

if __name__ == "__main__":
    sol = Solution()

    val = 3
    nums =[3,3]

    x = sol.removeElement(nums,val)
    print(x)

