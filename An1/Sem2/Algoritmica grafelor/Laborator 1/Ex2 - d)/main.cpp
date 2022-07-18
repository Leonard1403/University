#include <bits/stdc++.h>

using namespace std;

ifstream fin("in.txt");

const int CMAX = 1e4+15;
int graf[CMAX][CMAX];
bool viz[CMAX];
int n;
queue < int > Q;
void read()
{
    fin >> n;
    int x , y;
    while(fin >> x >> y)
    {
        graf[x][y] = 1;
        graf[y][x] = 1;
    }
}

void sout()
{
    cout << "Matricea de adiacenta: " << '\n';
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=n;j++)
            cout << graf[i][j] << " ";
        cout << '\n';
    }
    cout << '\n';
}

void bfs(int nod)
{
    int curent;
    Q.push(nod);
    while(!Q.empty())
    {
        curent = Q.front();
        for(int i=1;i<=n;i++)
        {
            int vecin = i;
            if(graf[curent][vecin]==1&&viz[vecin]==0)
            {
                viz[vecin] = 1;
                Q.push(vecin);
            }
        }
        Q.pop();
    }
}

int main()
{
    bool ok;
    read();
    bfs(1);
    ok = 1;
    //consideram graful a fi conex
    // 1 reprezitna valoarea true
    for(int i=1;i<=n;i++)
    {
        if(viz[i]==0){
            ok = 0;
            break;
        }
    }
    if(ok==1)
        cout << "Graful este conex";
    else
        cout << "Graful nu este conex";
    cout << '\n';
    sout();
    return 0;
}
