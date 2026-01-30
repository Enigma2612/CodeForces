#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main(){
    int ntc;
    cin >> ntc;
    while(ntc--){
        string word;
        cin >> word;
        int n = word.length();
        cout << word.substr(0,n-2) << 'i' << endl;
    }

    return 0;
}