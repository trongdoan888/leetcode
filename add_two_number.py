"""Bạn được cho hai danh sách liên kết không rỗng, mỗi danh sách đại diện cho một số nguyên không âm. Các chữ số được lưu trữ theo thứ tự ngược lại , và mỗi nút của chúng chứa một chữ số duy nhất. Hãy cộng hai số này và trả về tổng dưới dạng một danh sách liên kết.
Bạn có thể giả định rằng hai số này không chứa bất kỳ số 0 nào đứng đầu, ngoại trừ chính số 0."""

def add_two_number(l1,l2):
    count_l1 = len(l1) - 1
    count_l2 = len(l2) - 1

    list_result = []
    remember_number = 0

    while count_l1 >= 0 or count_l2 >= 0 or remember_number:
        x = 0
        y = 0 

        if count_l1 >= 0:
            x = l1[count_l1]
        else: x = 0 

        if count_l2 >= 0:
            y = l2[count_l2]
        else: y = 0

        total = x + y + remember_number
        print(total)
        if total >= 10:
            remember_number = total // 10
            list_result.append(total % 10)
        else:
            list_result.append(total)
            remember_number = 0

        count_l1 -= 1
        count_l2 -= 1

    return list_result[::-1]

        
if __name__ == "__main__" :
    l1 = [2,3,6]
    l2 = [4,5,6]
    
    list_result = add_two_number(l1,l2)

    print(list_result)


# cách tối ưu hơn 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            columnSum = l1Val + l2Val + carry
            carry = columnSum // 10
            newNode = ListNode(columnSum % 10)
            curr.next = newNode
            curr = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummyHead.next