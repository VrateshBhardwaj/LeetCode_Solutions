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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
       ListNode Head = new ListNode(0);
       int carry=0;
       ListNode p=l1,q=l2,curr=Head;
       //int len1=0,len2=0;
    //    while(p!=null)
    //    {
    //        len1++;
    //        p=p.next;
    //    }
    //    while(q!=null)
    //    {
    //        len2++;
    //        q=q.next;    
    //    }
    //    p=l1;
    //    q=l2;
    //    if(len1>len2)
    //    {
    //        for(int i=0;i<len1-len2;i++)
    //        {
    //            ListNode node = new ListNode(0);
    //            node.next=q;
    //            q=node;
    //        }
    //    }
    //    else if(len2>len1)
    //    {
    //        for(int i=0;i<len2-len1;i++)
    //        {
    //            ListNode node = new ListNode(0);
    //            node.next = p;
    //            p = node;
    //        }
    //    }
       while(q!=null || p!=null)
       {
           int x = (p!=null)?p.val:0;
           int y = (q!=null)?q.val:0;
           int sum = x + y + carry;
           carry = sum / 10; // update carry for next iteration
           curr.next = new ListNode(sum % 10);
           curr = curr.next;
           if(p!=null) p = p.next;
           if(q!=null) q = q.next;

           }
        if (carry>0)
        {
            curr.next = new ListNode(carry);
        }
           return Head.next;
       }
     }
