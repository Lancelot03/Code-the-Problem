
class Solution{
public:
  string rremove(string s){
    string ans;
    int n = s.length();
    for(int i = 0; i < s.length(); i++){
        if((i > 0 && s[i - 1] == s[i]) || (i + 1 < s.length() && s[i + 1] == s[i])){
            continue;
        }
        else{
            ans += s[i];
        }
    }
    return ans.length() == s.length() ? ans : rremove(ans);
}
};
