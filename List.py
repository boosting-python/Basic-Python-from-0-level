a = [1, 2, 3]    #List
print(a)         #print list
a.append(5)      #Add element in list
print(a)         #print list with adding 5 at last
a.pop()          #Remove last element in list
print(a)         #print list finally

'''
// Interview_bit
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

int Solution::lPalin(ListNode* A) {
    ListNode* start = A;
    //ListNode* end = A;
    //ListNode* prev;
    //copy list
    struct ListNode* new_node =(struct ListNode*) malloc(sizeof(struct ListNode)); 
    new_node = start;
    
    ListNode* new_node_save = new_node;
    
    new_node->val = start->val;
    start = start->next;
    while(start != NULL)
    {
        struct ListNode* new_node1 =(struct ListNode*) malloc(sizeof(struct ListNode));
        new_node->next = new_node1;
        new_node = new_node->next;
        new_node->val = start->val;
        start = start->next;
    }
    
    ListNode* head = new_node_save;
    ListNode* prev = NULL;
    ListNode* agla = NULL;
    
    //reverse;
    while(head != NULL)
    {
        agla = head->next;
        head->next = prev;
        prev = head;
        head = agla;
    }
    head = prev;
    int yes = 1;
    
    while(A!= NULL)
    {
        //cout<<new_node_save->val<<" ";new_node_save = new_node_save->next;
        cout<<A->val<<" ";A=A->next;
        
    }
    //check
    /*cout<<"head"<<head->val<<"A"<<A->val<<" ";
    while(head != NULL && A != NULL )
    {
        if(head->val == A->val)
        {   
            cout<<"head"<<head->val<<"A"<<A->val<<" ";
        }
        else
        {
            yes = 0;
            break;
        }
        head = head->next;
        A = A->next;
    }*/
    return yes;
    
}
XXXXXXXXXXXXXXXXXX
YYYYYYYYYYYYYYY
ZZZZZZZZZZZ
QQQQQQQQQQ
WWWWWWWWW
'''
