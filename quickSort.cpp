#include <bits/stdc++.h>
using namespace std;

int partion(int arr[],int s,int e){
  int pivot = arr[e];
  int i= s,j= s;
  while(j<e){
    if(arr[j]<=pivot){
      swap(arr[i],arr[j]);
      i++;
    }
    j++;
  }
  swap(arr[i],arr[e]);
  return i;
}

void quickSort(int arr[],int s,int e){
  if(s>=e){
    return;
  }
  int m = partion(arr,s,e);
  quickSort(arr,s,m-1);
  quickSort(arr,m+1,e);
}
  
int main()
{
 
    int n;
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++){
      cin>>arr[i];
    }
    quickSort(arr,0,n-1);
    for(int i=0;i<n;i++){
      cout<<arr[i]<<" ";
    }
    
  return 0;
}