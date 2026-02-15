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

    private int getlen(ListNode temp){
        int len = 0;
        while(temp != null){
            temp = temp.next;
            len++;
        }
        return len;
    }

    public ListNode swapNodes(ListNode head, int k) {

        int len = getlen(head);

        ListNode temp = head;
        int[] sol = new int[2];

        // First pass: store values
        for(int i = 0; i < len; i++){
            if(i == k - 1) sol[0] = temp.val;
            if(i == len - k) sol[1] = temp.val;
            temp = temp.next;
        }

        // Reset temp
        temp = head;

        // Second pass: swap values
        for(int i = 0; i < len; i++){
            if(i == k - 1) temp.val = sol[1];
            if(i == len - k) temp.val = sol[0];
            temp = temp.next;
        }

        return head;
    }
}
