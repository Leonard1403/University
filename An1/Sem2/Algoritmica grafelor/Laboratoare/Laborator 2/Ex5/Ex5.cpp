#include <bits/stdc++.h>

using namespace std;

ifstream fin("graf.txt");

const int CMAX = 1e4+15;
vector < int > graf[CMAX];
int n;
bool viz[CMAX];

void read()
{
    int x, y;
    fin >> n;
    while(fin >> x >> y)
    {
        graf[x].push_back(y);
        graf[y].push_back(x);
    }
}

void dfs(int nod)
{
    viz[nod] = 1;
    for(int i=0;i<graf[nod].size();i++)
    {
        int vecin = graf[nod][i];
        if(viz[vecin]==0)
        {
            cout << vecin << " ";
            dfs(vecin);
        }
    }
}

void afis_graf()
{
    for(int i=1;i<=n;i++)
    {
        cout << i << ": ";
        for(int j=0;j<graf[i].size();j++)
            cout << graf[i][j] << " ";
        cout << '\n';
    }
}
int main()
{
    read();
    cout << "Varfurile afisate din apelul recursiv al grafului sunt: ";
    for(int i=1;i<=n;i++)
    {
        if(viz[i]==0){
            cout << i << " ";
            dfs(i);
        }
    }
    cout << '\n';
    afis_graf();
    return 0;
}
