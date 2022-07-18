#include <bits/stdc++.h>

using namespace std;

const int CMAX = 1e4+15;
vector < int > G[CMAX];
int viz[CMAX];
int n , m;
int descoperire[CMAX] , finalizare[CMAX];
int _time;

void citre(){
    int x , y;
    cin >> n >> m;
    for(int i=1;i<=m;i++)
    {
        cin >> x >> y;
        G[x].push_back(y);
    }
}

void DFS_VISIT(int nod){
    _time = _time + 1;
    descoperire[nod] = _time;
    viz[nod] = 1;
    for(int j=0;j<G[nod].size();j++){
        if(viz[G[nod][j]]==0){
            DFS_VISIT(G[nod][j]);
        }
    }
    _time = _time + 1;
    finalizare[nod] = _time;
}

void DFS(int start){
    for(int i=0;i<n;i++)
    {
        viz[i] = 0;
    }
    _time = 0;
    DFS_VISIT(start);
    for(int i=0;i<n;i++){
        if(viz[i]==0)
        {
            DFS_VISIT(i);
        }
    }
}


int main()
{
    citre();
    for(int j=0;j<n;j++){
        DFS(j);
        cout << "Pornind de la nodul: " << j << '\n';
        for(int i=0;i<n;i++)
        {
            cout << "Nodul: " << i << " Timpul de descoperire: " << descoperire[i] << " Timpul de finalizare: " << finalizare[i] << '\n';
        }
        cout << '\n';
    }
    return 0;
}
