"""Cho hai mảng đã được sắp xếp nums1 và nums2 có kích thước lần lượt là m và n, hãy trả về giá trị trung vị của hai mảng đó."""

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        self.nums1 = nums1
        self.nums2 = nums2

        nums1 = nums1 + nums2
        nums1.sort()

        
        if len(nums1) % 2 == 0:
            x = len(nums1)/2 - 1
            median = ( nums1[int(x)] + nums1[int(x) + 1]) / 2

        else:
            x = (len(nums1) - 1 ) / 2  
            median = nums1[int(x)] 

        return median
    


if __name__ == "__main__":
    sol = Solution()

    nums1 = [1,3]
    nums2 = [2]

    nums3 = sol.findMedianSortedArrays(nums1,nums2)

    print(nums3)
