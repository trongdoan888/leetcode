"""Bạn được cho phần tử đầu tiên của hai danh sách liên kết đã được sắp xếp list1và list2.

Ghép hai danh sách thành một danh sách đã được sắp xếp . Danh sách này được tạo ra bằng cách nối các phần tử của hai danh sách đầu tiên lại với nhau.

Trả về phần tử đầu tiên của danh sách liên kết đã được hợp nhất .

 """

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: list, list2: list):
        cur = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
             
            else:
                cur.next = list2
                list2, cur = list2.next, list2
            
        if list1 or list2:
            cur.next = list1 if list1 else list2
        

        return dummy.next

        


        
  