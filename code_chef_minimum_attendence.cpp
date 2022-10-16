/*A semester in Chef’s University has 120 working days. The University’s requirement is that a student should be present for at least 75%of the working days in the semester. If not, the student is failed.

Chef has been taking a lot of holidays, and is now concerned whether he can pass the attendance requirement or not. NN working days have already passed, and you are given Nbits – B1, B2, …, BN. Bi = 0 denotes that Chef was absent on the ith day, and Bi = 11 denotes that Chef was present on that day.

Can Chef hope to pass the requirement by the end of the semester?*/


#include <iostream>
using namespace std;
int main() {
	int t;
	cin>>t;
	while(t--)
	{
	    int n,count=0;
	    cin>>n;
	    string s;
	    cin>>s;
	    for(int i=0;i<n;i++){
	    if(s[i]=='1')
	    count++;
	    }
	    int p=count+120-n;
	    float x=(p*100)/120;
	    if(x>=75)
	    cout<<"YES"<<endl;
	    else
	    cout<<"NO"<<endl;
	}
	return 0;
}
/*
Sample Input 1
3
50
00000000000000000000000000000000000000000000000000
50
01010101010101010101010101010101010101010101010101
2
01
Sample Output 1
NO
YES
YES
*/
