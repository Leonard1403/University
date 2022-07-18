#include <bits/stdc++.h>

using namespace std;

ifstream fin("in.txt");

const int CMAX = 1e3+15;
long long int n;
vector < int > graf[CMAX];
int matrice_adiacenta[CMAX][CMAX];
bool viz[CMAX][CMAX];
vector < pair < int , int > > muchii;
int matrice_incidenta[CMAX][CMAX];

void read()
{
    int x , y;
    fin >> n;
    while(fin >> x >> y)
    {
        graf[x].push_back(y);
        graf[y].push_back(x);
        matrice_adiacenta[x][y] = 1;
        matrice_adiacenta[y][x] = 1;
    }
}

void show_matrice_adiacenta()
{
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=n;j++)
        {
            cout << matrice_adiacenta[i][j] << " ";
        }
        cout << '\n';
    }
}

void show_lista_adiacenta()
{
    for(int i=1;i<n;i++)
    {
        sort(graf[i].begin(),graf[i].end());
        cout << i << ": ";
        for(int j=0;j<graf[i].size();j++)
        {
            if(viz[i][graf[i][j]]==0){
                muchii.push_back({i,graf[i][j]});
                viz[i][graf[i][j]] = 1;
                viz[graf[i][j]][i] = 1;
            }
            cout << graf[i][j] << " ";
        }
        cout << '\n';
    }
}

void show_matrice_incidenta()
{
    cout << "Lista muchiilor: " << '\n';
    for(int i=0;i<muchii.size();i++)
    {
        cout << "[" << muchii[i].first << " " << muchii[i].second << "] ;";
    }
    cout << '\n';

    for(int i=1;i<=n;i++)
    {
        for(int j=0;j<muchii.size();j++)
        {
            if(muchii[j].first == i||muchii[j].second==i)
                matrice_incidenta[i][j+1] = 1;
        }
    }

    for(int i=1;i<=n;i++)
    {
        for(int j=0;j<muchii.size();j++)
        {
            cout << matrice_incidenta[i][j+1] << " ";
        }
        cout << '\n';
    }
}

int main()
{
    read();
    cout << "Matricea de adiacenta: " << '\n';
    show_matrice_adiacenta();
    cout << '\n';
    cout << "Lista de adiacenta: " << '\n';
    show_lista_adiacenta();
    cout << '\n';
    cout << "Matricea incidenta: " << '\n';
    show_matrice_incidenta();
    cout << '\n';
    return 0;
}
