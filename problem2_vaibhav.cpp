#include <iostream>
#include <bits/stdc++.h>
using namespace std;
int main() 
{
    vector <int> a;
    a.push_back(1);
    a.push_back(2);
    int s = 0;
    int i = 0;
    int x = 0;
    int j;
    int cons = 4000000;
    while(true)
    {
           x = a[i] + a[i+1];
           if(x<cons)
           {
               a.push_back(x);
           }
           else
           {
               break;
           }
        i++;
    }
    for(j=1;j<a.size();j=j+3)
    {
            s = s + a[j];
    }
    cout<<s;
    return 0;
}
