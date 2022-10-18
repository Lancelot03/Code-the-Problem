#include <bits/stdc++.h>
using namespace std;
bool ispossible(vector<int> &stalls, int k,int mid)
{
    int cc=1,last=stalls[0];
    for(int i=0;i<stalls.size();i++)
    {
        if(stalls[i]-last>=mid)
        {
            cc++;
            if(cc==k)
                return true;
            last=stalls[i];
        }
    }
    return false;
}
int aggressiveCows(vector<int> &stalls, int k)
{
    //    Write your code here.
    sort(stalls.begin(),stalls.end());
    int s=0,maxi=-1;
    for(int i=0;i<stalls.size();i++)
    {
        maxi=max(maxi,stalls[i]);
    }
    int e=maxi,res=-1;
    int mid=s+(e-s)/2;
    while(s<=e)
    {
        if(ispossible(stalls,k,mid))
        {
            res=mid;
            s=mid+1;
        }
        else
        {
            e=mid-1;
        }
        mid=s+(e-s)/2;
    }
    return res;
}

int main()
{
    int t;
    cout<<"No of test cases : "<<endl;
    cin>>t;
    while(t--)
    {
        int n,k,a;
        vector<int>stalls;
        cout<<"Enter the total no. of elements in the array and cows : ";
        cin>>n>>k;
        cout<<"Enter the no. of pages in n books : "<< endl;
         for(int i=0 ; i<n ; i++)
    {
        cin>>a;
        stalls.push_back(a);
    }
    cout<<"Majority element in the seprated lines : ";
    int res=aggressiveCows(stalls, k);
    cout<<res<<endl;
    }
}

