#include <bits/stdc++.h>

using namespace std;

ifstream fin("graf.txt");

const int CMAX = 1e3+15;
vector < int > graf[CMAX];
queue < int > Q;
vector < pair < int , int > > muchii;

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
                muchii.push_back({nod,vecin});
                distanta[vecin] = distanta[nod] + 1;
                Q.push(vecin);
            }
        }
        Q.pop();
    }
}

void afis_muchii()
{
    for(int i=0;i<muchii.size();i++)
            cout << "[" << muchii[i].first << " " << muchii[i].second << "] ";
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
    afis_muchii();
    return 0;
}
