/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        
        if (list1 == null && list2 == null)
            return list1;
        else if (list1 == null)
            return list2;
        else if (list2 == null)
            return list1;
        ListNode result;
        if (list1.val <= list2.val) {
            result = createMergedList(list1, list2);
        }
        else {
            result = createMergedList(list2, list1);
        }
        return result;
    }
    
    private ListNode createMergedList(ListNode l1, ListNode l2) {
        ListNode result = new ListNode(l1.val,null);
        ListNode retRes = result;
        while (l1.next != null) {
            l1 = l1.next;
            while (l2 != null && l2.val <= l1.val) {
                result.next = new ListNode(l2.val, null);
                result = result.next;
                l2 = l2.next;
            }
            result.next = new ListNode(l1.val, null);
            result = result.next;
        }
        while (l2 != null) {
            result.next = new ListNode(l2.val, null);
            result = result.next;
            l2 = l2.next;
        }
        return retRes;
    }
}