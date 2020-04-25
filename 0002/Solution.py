from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    # 重载打印函数
    def __str__(self):
        ret = []
        cur = self
        while cur != None:
            ret.append(cur.val)
            cur = cur.next
        return str(ret)

    # 重载==运算符，注意!= 也会走进来
    def __eq__(self, other):
        if other == None:
            return False

        cur_self = self
        cur_other = other
        while cur_self != None and other != None:
            if cur_self.val != cur_other.val:
                return False
            cur_self = cur_self.next
            cur_other = cur_other.next

        if cur_self != None or cur_other != None:
            return False
        return True


def fill_ListNode(x):
    ret = ListNode(x[0])
    cur_node = ret
    for num in x[1:]:
        cur_node.next = ListNode(num)
        cur_node = cur_node.next

    return ret


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ret = ListNode(0)

        cur = ret
        while l1 != None or l2 != None:
            num1 = 0
            num2 = 0
            if (l1 != None):
                num1 = l1.val
                l1 = l1.next
            if (l2 != None):
                num2 = l2.val
                l2 = l2.next

            sum = num1 + num2 + cur.val
            jinwei = sum // 10
            cur.val = sum - jinwei * 10
            if jinwei != 0 or l1 != None or l2 != None:
                cur.next = ListNode(jinwei)
                cur = cur.next

        return ret


if __name__ == '__main__':
    s = Solution()

    ret = s.addTwoNumbers(l1=fill_ListNode([2, 4, 3]), l2=fill_ListNode([5, 6, 4]))
    print(ret)
    assert ret == fill_ListNode([7, 0, 8])
