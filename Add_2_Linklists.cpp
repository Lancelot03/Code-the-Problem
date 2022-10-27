/*You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit.
 Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.*/

/*Example : Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.*/

#include <bits/stdc++.h> 
using namespace std;

struct ListNode {
     int val;
     ListNode *next;
     ListNode() : val(0), next(nullptr) {}
     ListNode(int x) : val(x), next(nullptr) {}
     ListNode(int x, ListNode *next) : val(x), next(next) {}
 };
 
class Solution {
public:
    string findSum(string str1, string str2)
{
    
    if (str1.length() > str2.length())
        swap(str1, str2);
 
   
    string str = "";
 
   
    int n1 = str1.length(), n2 = str2.length();
 
   
    reverse(str1.begin(), str1.end());
    reverse(str2.begin(), str2.end());
 
    int carry = 0;
    for (int i=0; i<n1; i++)
    {
      
        int sum = ((str1[i]-'0')+(str2[i]-'0')+carry);
        str.push_back(sum%10 + '0');
 
        
        carry = sum/10;
    }
 
    
    for (int i=n1; i<n2; i++)
    {
        int sum = ((str2[i]-'0')+carry);
        str.push_back(sum%10 + '0');
        carry = sum/10;
    }
 
   
    if (carry)
        str.push_back(carry+'0');
 
    // reverse resultant string
    reverse(str.begin(), str.end());
 
    return str;
}
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        
        ListNode* temp = l1;
        string num1, num2;
        while(temp!=NULL){
            
            string s = to_string(temp->val);
            num1.append(s);
            temp = temp -> next;
        }
        
        reverse(num1.begin(), num1.end());
        
        temp = l2;
        while(temp!=NULL){
            
            string s = to_string(temp->val);
            num2.append(s);
            temp = temp -> next;
        }
        reverse(num2.begin(), num2.end());
        string final = findSum(num1,num2);
        ListNode* head = NULL;
        ListNode* tail = NULL;
        
        if(final == "0" ){
            
            ListNode* newnode = new ListNode(0);
            newnode->next = NULL;
            return newnode;
        }
        for(int i = final.length() ; i>0 ;i--){
            
            ListNode* newnode = new ListNode(final[i-1]-'0');
            if(head==NULL){
                head = newnode;
                tail = newnode ;
            }else{
                tail->next = newnode;
                tail= tail->next;
            }
            
            
        }
        tail->next = NULL;
        return head;
    }
};