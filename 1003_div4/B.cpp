#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main(){
    int ntc;
    cin >> ntc;
    vector<int> ans;
    for(int _=0; _<ntc; _++){
        string word;
        cin >> word;
        bool flag = false;
        for(int i=0; i<word.length()-1; i++){
            if(word[i]==word[i+1]){
                ans.push_back(1);
                flag = true;
                break;
            }
        }
        if(!flag){
            ans.push_back(word.length());
        }
    }
    for(int el: ans){cout << el<<endl;}

    return 0;
}