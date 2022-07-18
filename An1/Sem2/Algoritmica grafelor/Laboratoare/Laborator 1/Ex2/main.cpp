#include <bits/stdc++.h>

using namespace std;

ifstream fin("in.txt");

const int CMAX = 1e3+15;
int n;
int matricea_adiacenta[CMAX][CMAX];
int matricea_distantelor[CMAX][CMAX];
int dist;
vector < int > graf[CMAX];
queue < int > Q;

bool viz[CMAX];

void read()
{
    int x , y;
    fin >> n;
    while(fin >> x >> y)
    {
        graf[x].push_back(y);
        graf[y].push_back(x);
        matricea_adiacenta[x][y] = 1;
        matricea_adiacenta[y][x] = 1;
    }
}

void bfs(int nod)
{
    int curent;
    Q.push(nod);
    viz[nod] = 1;
    dist = 0;
    while(Q.size())
    {
        nod = Q.front();
        cout << nod << " ";
        for(int i=0;i<graf[nod].size();i++)
        {
            curent = graf[nod][i];
            if(viz[curent] == 0)
            {
                viz[curent] = 1;
                matricea_distantelor[nod][curent] = dist + 1;
                Q.push(curent);
            }
        }
        Q.pop();
        dist=dist + 1;
    }
}

void show_noduri_izolate()
{
    cout << "Varfuri izolate: " << '\n';
    bool ok = 0;
    for(int i=1;i<=n;i++)
    {
        if(graf[i].size()==0){
            cout << "Varful " << i << " este izolat" << '\n';
            ok = 1;
        }
    }
    if(ok==0)
        cout << "Nu sunt varfuri izolate";
    cout << '\n' << '\n';
}

void show_graf_regular()
{
    cout << "Graf regular: " << '\n';
    int da;
    da = graf[1].size();
    for(int i=2;i<=n;i++)
    {
        if(graf[i].size()!=da){
            cout << "Graful nu este regular";
            cout << '\n' << '\n';
            return;
        }
    }
    cout << "Graful este regular" << '\n';
    cout << '\n' << '\n';
}

void show_matricea_distantelor()
{
    cout << "Matricea distantelor: " << '\n';
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=n;j++)
        {
            cout << matricea_distantelor[i][j] << " ";
        }
        cout << '\n';
    }
    cout << '\n' << '\n';
}

int main()
{
    read();
    show_noduri_izolate();
    show_graf_regular();

    /*
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=n;j++)
            viz[j] = 0;
        if(viz[i]==0){
            cout << "i: ";
            bfs(i);
            cout << '\n';
        }
    }
    */

    //show_matricea_distantelor();

    return 0;
}
