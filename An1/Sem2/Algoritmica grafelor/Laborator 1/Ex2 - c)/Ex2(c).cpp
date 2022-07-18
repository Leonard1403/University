#include <bits/stdc++.h>

using namespace std;

ifstream fin("in.txt");

const int CMAX = 1e4+15;
int graf[CMAX][CMAX];
int dist[CMAX][CMAX];
int viz[CMAX];
int n;
queue < int > Q;

// n = nr noduri
// graf[n][n] - graful reprezentat sub forma de matrice de adiacenta

void read()
{
    int x , y;
    fin >> n;
    while(fin >> x >> y)
    {
        graf[x][y] = graf[y][x] = 1;
    }
}

void disout()
{
    cout << "Matricea distantelor: " << '\n';
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=n;j++)
            cout << dist[i][j] << " ";
        cout << '\n';
    }
    cout << '\n';
}

void dfs(int curent, int nod, int distanta)
{
    //disout();
    //cout << "distanata: " << distanta << " ";
    dist[curent][nod] = distanta;
    viz[nod] = 1;
    for(int i=1;i<=n;i++)
    {
        if((graf[nod][i]==1&&viz[i]==0)||(graf[nod][i]==1&&dist[curent][nod]+1<dist[curent][i])){
            //cout << "intrat: " << i << " ";
            dfs(curent,i,distanta+1);
            //cout << "intors: " << i << " ";
        }
    }
    //cout << '\n';
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

int main()
{
    read();
    int inf = CMAX;
    for(int i=1;i<=n;i++)
        for(int j=1;j<=n;j++)
            dist[i][j] = inf;
    for(int i=1;i<=n;i++)
    {
        memset(viz,0,sizeof(viz));
        viz[i] = 1;
        dfs(i, i ,0);
    }
    sout();
    cout << '\n';
    disout();
    return 0;
}
