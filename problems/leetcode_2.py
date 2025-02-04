# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        val1=l1.val if l1.val is not None else 0
        val2=l2.val if l2.val is not None else 0
        head = ListNode((val1+val2)%10)
        current=head
        current_node_1=l1.next
        current_node_2=l2.next
        up_value=1 if (l1.val+l2.val)>=10 else 0
        while current_node_1!=None or current_node_2 !=None or up_value!=0 :
            val1 = current_node_1.val if current_node_1 is not None else 0
            val2 = current_node_2.val if current_node_2 is not None else 0
            new_node=ListNode((val1+val2+up_value)%10)
            current.next=new_node
            current=new_node
            up_value=(val1+val2+up_value)//10
            current_node_1 = current_node_1.next if current_node_1 is not None else None
            current_node_2 = current_node_2.next if current_node_2 is not None else None
        return head