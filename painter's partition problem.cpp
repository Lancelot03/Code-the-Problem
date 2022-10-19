#include<bits/stdc++.h>
using namespace std;
bool ispossible(vector<int>arr,int n,int m,int mid)
{
    int sc=1,ps=0;
    for(int i=0;i<n;i++)
    {
        if(ps+arr[i]<=mid)
        {
            ps+=arr[i];
        }
        else
        {
            sc++;
            if(sc>m||arr[i]>mid)
            {
                return false;
            }
            ps=arr[i];
        }
    }
    return true;
}
int findLargestMinDistance(vector<int> &arr, int k)
{
    //    Write your code here.
    int n=arr.size();
     int s=0,sum=0;
    for(int i=0;i<n;i++)
    {
        sum+=arr[i];
    }
    int e=sum,ans=-1,mid;
    mid=s+(e-s)/2;
    while(s<=e)
    {
        if(ispossible(arr,n,k,mid))
        {
            ans=mid;
            e=mid-1;
        }
        else
        {
            s=mid+1;
        }
        mid=s+(e-s)/2;
    }
    return ans;
}
int main()
{
    int t;
    cout<<"No of test cases : "<<endl;
    cin>>t;
    while(t--)
    {
        int n,k,a;
        vector<int>arr;
        cout<<"Enter the total no. of element in the array and available painters : ";
        cin>>n>>k;
        cout<<"Enter the no. element in the array : "<< endl;
         for(int i=0 ; i<n ; i++)
    {
        cin>>a;
        arr.push_back(a);
    }
    int res=findLargestMinDistance(arr,k);
    cout<<"Minimum time : ";
    cout<<res<<endl;
    }
}
