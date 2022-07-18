#include <bits/stdc++.h>

using namespace std;

ifstream fin("graf.txt");

const int CMAX = 1e4+15;
queue < int > Q;
int mat[CMAX][CMAX];
int new_mat[CMAX][CMAX];
bool viz[CMAX];
int n;

void read()
{
    fin >> n;
    int x , y;
    while(fin >> x >> y)
    {
        mat[x][y] = 1;
        new_mat[x][y] = 1;
    }
    for(int i=0;i<n;i++){
        mat[i][i] = 1;
        new_mat[x][y] = 1;
    }
}

void afisare()
{
    cout << "Afisare: \n";
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            cout << mat[i][j] << " ";
        }
        cout << '\n';
    }
}

void new_afisare()
{
    cout << "New Afisare: \n";
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            cout << new_mat[i][j] << " ";
        }
        cout << '\n';
    }
}
void bfs(int nod)
{
    int curent;
    Q.push(nod);
    while(!Q.empty())
    {
        curent = Q.front();
        Q.pop();
        for(int i=0;i<n;i++)
        {
            int vecin = i;
            if(mat[curent][vecin]==1&&viz[vecin]==0)
            {
                Q.push(vecin);
                viz[vecin] = 1;
            }
        }
    }
}

int main()
{
    read();
    afisare();
    for(int i=0;i<n;i++)
    {
        memset(viz,0,sizeof(viz));
        bfs(i);
        for(int j=0;j<n;j++)
            if(viz[j]==1)
                new_mat[i][j] = 1;

    }
    cout << '\n';
    new_afisare();
    return 0;
}
