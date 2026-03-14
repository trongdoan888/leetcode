"""Cho một mảng số nguyên nums, hãy trả về tất cả các bộ ba [nums[i], nums[j], nums[k]]sao cho i != j, i != k, và j != k, và nums[i] + nums[j] + nums[k] == 0.

Lưu ý rằng tập hợp lời giải không được chứa các bộ ba trùng lặp."""


class Solution:
    def threeSum(self, nums):
        ans=set()
        nums.sort()
        n=len(nums)

        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    temp=nums[i]+nums[j]+nums[k]
                    if temp==0:
                        ans.add((nums[i],nums[j],nums[k]))

        lst = list(ans)
        return lst

if __name__ == "__main__":
    sol = Solution()

    nums = [-100,-70,-60,110,120,130,160]

    x = sol.threeSum(nums)
    
    print(x)

    
