#include <bits/stdc++.h>

using namespace std;

ifstream fin("graf.txt");

const int CMAX = 1015;
vector < int > graf[CMAX];
int matricea_distantelor[CMAX][CMAX];
int matricea_adiacenta[CMAX][CMAX];
int n;

void read()
{
    fin >> n;
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=n;j++)
        {
            fin >> matricea_distantelor[i][j];
        }
    }
}

void afis_distantelor()
{
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=n;j++)
        {
            cout << matricea_distantelor[i][j] << " ";
        }
        cout << '\n';
    }
}

void afis_adiacenta()
{
    cout << "Matrice de adiacenta: " << '\n';
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=n;j++)
        {
            cout << matricea_adiacenta[i][j] << " ";
        }
        cout << '\n';
    }
}

void afis_lista()
{
    cout << "Lista de adiacenta: " << '\n';
    for(int i=1;i<=n;i++)
    {
        cout << i << ": ";
        for(int j=0;j<graf[i].size();j++)
        {
            cout << graf[i][j] << " ";
        }
        cout << '\n';
    }
}
int main()
{
    read();
    afis_distantelor();

    //inf == 1015(DOAR O VALOARE)

    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=n;j++)
        {
            for(int z=1;z<=n;z++)
            {
                if(z!=j)
                {
                    if(matricea_distantelor[i][j]+1==matricea_distantelor[i][z]&&matricea_distantelor[i][j]==0){
                        //cout << i << " " << j << " " << z << '\n';
                        matricea_adiacenta[z][j] = 1;
                        matricea_adiacenta[j][z] = 1;
                    }
                }
            }
        }
    }

    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=n;j++)
        {
            if(matricea_adiacenta[i][j]==1)
                graf[i].push_back(j);
        }
    }

    cout << '\n';
    afis_adiacenta();
    cout << '\n';
    afis_lista();
    return 0;
}
