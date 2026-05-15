"""Bạn đang leo cầu thang. Cần phải leo ntừng bậc để lên đến đỉnh.

Mỗi lần bạn có thể leo lên 1hoặc 2bước xuống. Hỏi có bao nhiêu cách khác nhau để leo lên đỉnh?"""


class Solution:
    def climbStairs(self, n: int) -> int:

        def giaithua(x):
            if x == 0 or x == 1:
                return 1
            return x * giaithua(x - 1)

        count = 0

        # a = số bước đi 2 bậc
        for a in range(n // 2 + 1):

            one = n - 2 * a      # số bước 1 bậc
            total = one + a      # tổng số lượt đi

            count += giaithua(total) // (
                giaithua(a) * giaithua(one)
            )

        return count

