/*
Submitted by: Sneha jaiswal
gutHub link: https://github.com/Sneha-jais 
panagram is a sentence containing every letter of english alphabet
"We promptly judged antique ivory buckles for the next prize"
Input: “The quick brown fox jumps over the lazy dog” 
Output: is a Pangram 
Explanation: Contains all the characters from ‘a’ to ‘z’] 
*/

#include <bits/stdc++.h>
using namespace std;
bool panagram(string str)
{
    int count = 0;
    int index;
    bool marks[26] = {false};
    for (int i = 0; i < str.length(); i++)
    {
        if (str[i] >= 'a' && str[i] <= 'z')
            index = str[i] - 'a';
        else if (str[i] >= 'A' && str[i] <= 'Z')
            index = str[i] - 'A';
        else
            continue;
        marks[index] = true;
    }
    for (int i = 0; i < 26; i++)
    {
        if (marks[i] == false)
            return false;
    }
    return true;
}

int main()
{
    string s;
    getline(cin, s);
    if (panagram(s) == true)
        cout << "Given string is a Pangram\n";
    else
        cout << "Given string is not a Pangram\n";
    return 0;
}
