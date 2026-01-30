#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main(){
    int ntc;
    cin >> ntc;
    while(ntc--){
        int n;
        vector<int> arr;
        cin >> n;
        vector<int> freq(n+1);
        for(int _=0; _<n;_++){
            int el;
            cin >> el;
            freq[el] += 1;
            arr.push_back(el);
        }
        int p1=0, p2=1;
        int score=0;
        int len_left=n-(p2-p1);
        while(p2 < n){
        }
    }

    return 0;
}