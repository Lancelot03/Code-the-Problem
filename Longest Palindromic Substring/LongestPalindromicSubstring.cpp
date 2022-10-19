#include <bits/stdc++.h>
using namespace std;

int longestPalSubstr(string str) {
    int n = str.size();
    if (n < 2)
        return n;

    int maxLength = 1, start = 0;
    int low, high;
    for (int i = 0; i < n; i++) {
        low = i - 1;
        high = i + 1;
        while (high < n && str[high] == str[i])
            high++;

        while (low >= 0 && str[low] == str[i])
            low--;

        while (low >= 0 && high < n && str[low] == str[high]) {
            low--;
            high++;
        }

        int length = high - low - 1;
        if (maxLength < length) {
            maxLength = length;
            start = low + 1;
        }
    }

    cout << "Longest palindrome substring is: ";
    cout << str.substr(start, maxLength);
    return maxLength;
}

int main() {
    string str = "hacktoberfests";
    cout << "\nLength is: " << longestPalSubstr(str) << endl;
    return 0;
}
