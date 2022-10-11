#include<bits/stdc++.h>

using namespace std;

int solve(string str) {

  if(str.size()==0)
      return 0;
  int maxans = INT_MIN;
  for (int i = 0; i < str.length(); i++) 
  {
    unordered_set < int > set;
    for (int j = i; j < str.length(); j++) 
    {
      if (set.find(str[j]) != set.end())
      {
        maxans = max(maxans, j - i);
        break;
      }
      set.insert(str[j]);
    }
  }
  return maxans;
}

int main() {
  string str = "takeUforward";
  cout << "The length of the longest substring without repeating characters is " << 
  solve(str);
  return 0;
}
