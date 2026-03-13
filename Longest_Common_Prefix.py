"""Hãy viết một hàm để tìm chuỗi tiền tố chung dài nhất trong một mảng các chuỗi.

Nếu không có tiền tố chung, hãy trả về chuỗi rỗng ""."""


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        self.strs = strs
        pre = strs[0]
        
        for i in strs:
            while not i.startswith(pre):
                pre = pre[:-1]
        
        return pre         




if __name__ == "__main__":
    sol = Solution()

    strs = ["flower","flow","flight"]



