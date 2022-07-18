#include <bits/stdc++.h>

using namespace std;

ifstream fin("graf.txt");

const int CMAX = 1e3+15;
vector < int > graf[CMAX];
queue < int > Q;
int distanta[CMAX];
bool viz[CMAX];
int n;

void read()
{
    fin >> n;
    int x , y;
    while(fin >> x >> y)
    {
        graf[x].push_back(y);
        graf[y].push_back(x);
    }
}

void bfs(int nod,int dist)
{
    Q.push(nod);
    distanta[nod] = 0;
    while(!Q.empty())
    {
        nod = Q.front();
        cout << nod << " ";
        for(int i=0;i<graf[nod].size();i++)
        {
            int vecin = graf[nod][i];
            if(distanta[vecin]==CMAX)
            {
                distanta[vecin] = distanta[nod] + 1;
                Q.push(vecin);
            }
        }
        Q.pop();
    }
}

int main()
{
    read();
    for(int i=1;i<=n;i++)
    {
        distanta[i] = CMAX;
    }
    int nodul;
    cout << "Nodul: ";
    cin >> nodul;
    distanta[nodul] = 0;
    viz[nodul] = 1;
    cout << "Nodurile din apelul BFS sunt: ";
    bfs(nodul,1);
    cout << '\n';
    for(int i=1;i<=n;i++)
    {
        cout << "Distanta pana la nodul " << i << " este de " << distanta[i] << '\n';
    }
    return 0;
}
