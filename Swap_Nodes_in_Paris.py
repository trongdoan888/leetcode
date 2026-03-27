"""Cho một danh sách liên kết, hãy hoán đổi hai phần tử liền kề nhau và trả về phần tử đầu tiên của danh sách. Bạn phải giải quyết bài toán mà không được thay đổi giá trị trong các phần tử của danh sách (nghĩa là, chỉ có bản thân các phần tử mới được thay đổi)."""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head) :
        self.head = head 
        
        if not head or not head.next:
            return head
        
        first_node = head
        second_node = head.next


        first_node.next = self.swapPairs(second_node.next)

        second_node.next = first_node

        return second_node




        




    