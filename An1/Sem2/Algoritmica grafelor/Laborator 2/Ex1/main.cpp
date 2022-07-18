#include <bits/stdc++.h>

using namespace std;

ifstream fin("graf.txt");
const int CMAX = 1e4+15;
vector < int > graf[CMAX];
queue < int > Q;

int n;

void read()
{
    int x, y;
    fin >> n;
    while(fin >> x >> y)
    {
        graf[x].push_back(y);
        graf[y].push_back(x);
    }
}

void afisare()
{
    cout << "Afisare: \n";
    for(int i=1;i<=n;i++)
    {
        cout << i << ": ";
        for(int j=0;j<graf[i].size();j++)
        {
            cout << graf[i][j] << " ";
        }
        cout << '\n';
    }
    cout << '\n';
}

void moore(int curent,int lungime[], int parinte[])
{
    int x;
    lungime[curent] = 0;
    for(int i=1;i<=n;i++)
        if(i!=curent)
            lungime[i] = CMAX;
    Q.push(curent);
    while(!Q.empty())
    {
        x = Q.front();
        for(int i=0;i<graf[x].size();i++)
        {
            int vecin = graf[x][i];
            if(lungime[vecin]==CMAX)
            {
                parinte[vecin] = x;
                lungime[vecin] = lungime[x] + 1;
                Q.push(vecin);
            }
        }
        Q.pop();
    }
}

void lant(int nod,int parinte[])
{
    if(nod!=0){
        cout << nod << " ";
        lant(parinte[nod],parinte);
    }
}

int main()
{
    int nod_secund;
    int parinte[CMAX];
    int lungime[CMAX];
    read();
    afisare();
    int nod;
    cout << "Nod = ";
    cin >> nod;
    moore(nod,lungime,parinte);
    cout << "Lungime de la " << nod << ": \n";
    for(int i=1;i<=n;i++)
        cout << "Distanta de la" << nod << " pana la " << i << " este:" << lungime[i] << '\n';

    cout << '\n';
    cout << "Parintii: \n";
    for(int i=1;i<=n;i++)
        cout << "Parintele lui " << i << " este " << parinte[i] << '\n';
    cout << "Nod secund = ";
    cin >> nod_secund;
    lant(nod_secund,parinte);
    return 0;
}
