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
        //Fisier -> Matrice adiacenta
        matrice_adiacenta[x][y] = 1;
        matrice_adiacenta[y][x] = 1;
    }
}

void make_matrice_adiacenta2()
{
    int x, y;
    //Lista adiacenta -> Matrice adiacenta
    for(int i=1;i<=n;i++)
    {
        x = i;
        for(int j=0;j<graf[i].size();j++)
        {
            y = graf[i][j];
            matrice_adiacenta[x][y] = 1;
            matrice_adiacenta[y][x] = 1;
        }
    }
}

void show_matrice_adiacenta()
{
    cout << "Matrice adiacenta: \n";
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=n;j++)
        {
            cout << matrice_adiacenta[i][j] << " ";
        }
        cout << '\n';
    }
    cout << '\n';
}

void make_lista_adiacenta1()
{
    // Matrice adiacenta -> Lista adiacenta
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=n;j++)
        {
            if(matrice_adiacenta[i][j] == 1)
                graf[i].push_back(j);
        }
    }
}

void make_lista_adiacenta2()
{
    int m, x, y;
    // Matrice incidenta -> Lista adiacenta

    m = muchii.size();
    //m -> muchii
    //n -> noduri

    for(int i=1;i<=m;i++)
    {
        x = muchii[i-1].first;
        y = muchii[i-1].second;
        graf[x].push_back(y);
        graf[y].push_back(x);
    }
}

void show_lista_adiacenta()
{

    cout << "Lista adiacenta: \n";
    for(int i=1;i<=n;i++)
    {
        sort(graf[i].begin(),graf[i].end());
        cout << i << ": ";
        for(int j=0;j<graf[i].size();j++)
        {
            cout << graf[i][j] << " ";
        }
        cout << '\n';
    }
    cout << '\n';
}

void make_matrice_incidenta1()
{
    // Lista adiacenta -> Matrice incidenta
    for(int i=1;i<=n;i++)
    {
        for(int j=0;j<graf[i].size();j++)
        {
            if(viz[i][graf[i][j]] == 0)
            {
                muchii.push_back({i,graf[i][j]});
                viz[i][graf[i][j]] = 1;
                viz[graf[i][j]][i] = 1;
            }
        }
    }
}

void show_matrice_incidenta()
{
    cout << "Matrice incidenta: \n";
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
    cout << '\n';
}

int main()
{
    read();

    show_matrice_adiacenta();

    make_lista_adiacenta1();
    memset(matrice_adiacenta,0,sizeof(matrice_adiacenta));
    show_lista_adiacenta();

    make_matrice_incidenta1();
    for(int i=1;i<=n;i++)
        memset(graf,0,sizeof(graf));
    show_matrice_incidenta();

    make_lista_adiacenta2();
    for(int i=0;i<muchii.size();i++)
        muchii[i].first = muchii[i].second = 0;
    memset(matrice_incidenta,0,sizeof(matrice_incidenta));
    show_lista_adiacenta();

    make_matrice_adiacenta2();
    for(int i=1;i<=n;i++)
        memset(graf,0,sizeof(graf));
    show_matrice_adiacenta();
    return 0;
}
