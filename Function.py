
def product_function(x):    #Initialising a function product_function
    return 2 * x            #Multiply argument x by 2
a=product_function(5)       #when x=5 then a=2*5
print(a)                    #output 10


'''
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    cin>>T;
    while(T--)
    {
        int n,m,q;
        cin>>n>>m>>q;
        int x,y;
        int row[n]={0};
        int col[m]={0}; 
        for(int i=0;i<q;i++)
        {
            cin>>x>>y;
            row[x-1]++;
            col[y-1]++;
        }
        
        int count=0;
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {   //cout<<row[i]+col[j]<<" ";
                if((row[i]+col[j]) % 2 !=0)
                count++;
            }
        }
        cout<<count<<endl;
        /*
        for(int i=0;i<n;i++)
        cout<<row[i]<<" ";
        cout<<endl;
        
        for(int i=0;i<m;i++)
        cout<<col[i]<<" ";
        cout<<endl;*/
    }
}

//this is fine
