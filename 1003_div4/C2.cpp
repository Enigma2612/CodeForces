#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main(){
    int ntc;
    cin >> ntc;

    while(ntc--){
        int n,m;
        cin >> n >> m;
        vector<int> arr;
        vector<int> t_arr;
        vector<int> b;
        bool flag=true;
        for(int i=0; i<n; i++){
            int x;
            cin >> x;
            arr.push_back(x);
        }
        for(int _=0; _<m; _++){int x; cin >> x; b.push_back(x);}
        
        int prev = (t_arr[0] < arr[0] ? t_arr[0]-1 : arr[0]-1);
        for(int i=0; i<n; i++){
            int el1 = arr[i], el2 = t_arr[i];
            if(el1 >= prev && el2 >= prev){
                if(el1<el2){prev=el1;}
                else{prev=el2;}
            }
            else if (el1>=prev){ prev = el1;}
            else if (el2 >= prev){ prev = el2;}
            else{cout << "NO" << endl; flag=false; break;}
        }
        if(flag){cout << "YES" << endl;}

    }

    return 0;
}