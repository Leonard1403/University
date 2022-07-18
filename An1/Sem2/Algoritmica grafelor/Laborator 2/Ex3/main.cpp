#include <bits/stdc++.h>

using namespace std;

ifstream fin("labirint_cuvinte.txt");
ofstream fout("afis.txt");
const int CMAX = 1e3+15;
int mat[CMAX][CMAX];
int viz[CMAX][CMAX];
int n , m;
bool sol = 0;
pair < int , int > st , fn;
queue < pair < int , int > > Q;

int dx[] = {0 , 0 , -1 , +1};
int dy[] = {-1 , +1 , 0 , 0};

void read()
{
    char linie[CMAX];
    n = 0;
    while(fin.getline(linie,CMAX))
    {
        //cout << linie << '\n';
        m = strlen(linie);
        n = n + 1;
        for(int i=0;i<m;i++)
        {
            if(linie[i]=='S'){
                st = make_pair(n,i+1);
                mat[n][i+1] = 0;
                viz[n][i+1] = 0;
            }
            else if(linie[i]=='1'){
                mat[n][i+1] = 1;
                viz[n][i+1] = 1;
            }
            else if(linie[i]=='0'){
                mat[n][i+1] = 0;
                viz[n][i+1] = 0;
            }
            else if(linie[i]=='F'){
                mat[n][i+1] = 0;
                viz[n][i+1] = 0;
                fn = make_pair(n,i+1);
            }
        }
    }
}

bool verif(int cord_i , int cord_j)
{
    if(cord_i<1||cord_j<1||cord_i>n||cord_j>m||viz[cord_i][cord_j]!=0)
        return true;
    return false;
}

void just_mat()
{
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=m;j++)
            cout << mat[i][j];
        cout << '\n';
    }
    cout << '\n' << '\n';
}
void just_mat_fisier()
{
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=m;j++)
            fout << mat[i][j];
        fout << '\n';
    }
}
bool ok = 0;
void lee_rec(int cord_i, int cord_j)
{
    if(cord_i==fn.first&&cord_j==fn.second&&ok==0){
        just_mat();
        just_mat_fisier();
        fout << '\n';
        ok = 1;
    }
    else{
        for(int i=0;i<=3;i++)
        {
            int new_i , new_j;
            new_i = cord_i + dx[i];
            new_j = cord_j + dy[i];
            //cout << "cord_i: " << cord_i << " cord_j: " << cord_j << '\n';
            //cout << "new_i: " << new_i << " new_j: " << new_j << '\n';
            //cout << '\n';
            if(verif(new_i,new_j)!=true)
            {
                mat[cord_i][cord_j] = 9;

                viz[cord_i][cord_j] = 1;

                //cout << "cord_i: " << cord_i << " cord_j: " << cord_j << '\n';
                //cout << "new_i: " << new_i << " new_j: " << new_j << '\n';
                //just_mat();

                lee_rec(new_i,new_j);

                mat[cord_i][cord_j] = 0;
            }
        }
    }
}

void afis()
{
    cout << "n: " << n << " m: " << m << '\n';
    cout << "Poz_start: " << st.first << " " << st.second << " Poz_stop: " << fn.first << " " << fn.second << '\n';
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=m;j++)
        {
            cout << mat[i][j];
        }
        cout << '\n';
    }
}
int main()
{
    read();
    afis();
    cout << '\n';
    lee_rec(st.first,st.second);
    return 0;
}
