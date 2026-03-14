"""Cho một mảng số nguyên numscó độ dài nvà một số nguyên target, hãy tìm ba số nguyên tại các chỉ số khác nhau trong numssao cho tổng của ba số nguyên đó gần nhất với target.

Trả về tổng của ba số nguyên đó .

Bạn có thể giả định rằng mỗi đầu vào sẽ có chính xác một giải pháp."""

class Solution:
    def threeSumClosest(self, nums: list, target):
        self.nums = nums
        self.target = target
        nums.sort()
    
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) -2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):

                    total = nums[i] + nums[j] + nums[k]


                    if abs(total - target) < abs(result - target):
                        result = total
        
        return result

if __name__ == "__main__":
    sol = Solution()
    nums = [-1,2,1,-4]
    target = 1

    x = sol.threeSumClosest(nums,target)
    print(x)

    


