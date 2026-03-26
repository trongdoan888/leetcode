"""Cho trước ncác cặp dấu ngoặc đơn, hãy viết một hàm để tạo ra tất cả các tổ hợp dấu ngoặc đơn hợp lệ ."""

class Solution:
    def generateParenthesis(self, n: int):
        self.n = n
        
        ret = []

        def gen_par(k,balance,seq):
            if len(seq) == 2*n:
                ret.append(seq)
            
            if k > 0:
                gen_par(k-1, balance + 1, seq + "(")
            
            if balance > 0:
                gen_par(k, balance - 1, seq + ")")
            
        gen_par(n,0,"")
        return ret



 