#include <iostream>
#include <fstream>
#include <queue>
#include <vector>

#define pb push_back
using namespace std;

ifstream fin("dijkstra.in");
ofstream fout("dijkstra.out");

const int CMAX = 50015;
const int oo = 1<<31-1;

int n , m , D[CMAX] , x , y , z;
bool viz[CMAX];

struct comp{
    bool operator()(int x ,int y)
    {
        return D[x] > D[y];
    }
};

vector < pair < int , int > > v[CMAX];
priority_queue < int , vector < int > , comp > Q;

void citire()
{
    fin >> n >> m;
    for(int i=1;i<=m;i++)
    {
        fin >> x >> y >> z;
        v[x].pb({y,z});
    }
    for(int i=1;i<=n;i++)
        D[i] = oo;
}

void dijkstra(int nod)
{
    viz[nod] = 1;
    D[nod] = 0;
    Q.push(nod);

    while(!Q.empty())
    {
        int nodcurent;
        nodcurent = Q.top();
        viz[nodcurent] = 0;
        for(int i=0;i<v[nodcurent].size();i++)
        {
            int cost , vecin;
            vecin = v[nodcurent][i].first;
            cost = v[nodcurent][i].second;
            if(D[nodcurent]+cost<D[vecin])
            {
                D[vecin] = D[nodcurent] + cost;
                if(viz[vecin]==0)
                {
                    Q.push(vecin);
                    viz[vecin] = 1;
                }
            }
        }
        Q.pop();
    }
}

int main(int argc, char* argv[])
{
    //citire();
    ifstream fin(argv[1]);
    ofstream fout(argv[2]);

    int s;

    fin >> n >> m >> s;
    for(int i=1;i<=m;i++)
    {
        fin >> x >> y >> z;
        v[x].pb({y,z});
    }
    for(int i=1;i<=n;i++)
        D[i] = oo;


    dijkstra(s);
    for(int i=2;i<=n;i++)
    {
        if(D[i]==oo)
            fout << "INF" << " ";
        else fout << D[i] << " ";
    }

    fin.close();
    fout.close();
    return 0;
}
