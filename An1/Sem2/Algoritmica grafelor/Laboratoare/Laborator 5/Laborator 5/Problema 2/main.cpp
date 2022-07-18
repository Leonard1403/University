//MODIFICARE SURSA PENTRU IMPLEMENTARE 0
/*
                  __===*@@@ @@@@@ @@@@@
                 /       ________________________________________ ___ __ _ _
          ______|^|_    | ***                                    |___ ___ __
         /|/~~~~~~~|    |  ***                                   |____ __ _ __
        / |    {_) |    |   ***  My Source(Leo)                  |__ ___ _ __
   ____/__|)  /~~| |@@@@|    ************************************|____ ___ _
  / _____ ~~~~~~~~~|@@@@|     ***********************************|___ __ _ __
 | /     \\      --|    |_/~~~~~\_______________________/~~~~~\__|_____ __ _ _
 |/  ***  \\       |---~|/  ***  \_____________________/  ***  \_|___ _ __ _ _
 `  *****  ~~~~=====       *****                         *****
     ***                    ***                           ***
------------------------------------------------------------------------------
*/
//Acest algoritm este de pompare topologica

#include <bits/stdc++.h>

using namespace std;

const int NMAX = 1e3+5;

const string file = "10";

ifstream fin(file+"-in.txt");
ofstream fout(file+"-out.txt");

int n , m;

vector < int > graf[NMAX];
int cost[NMAX][NMAX], reziduri[NMAX][NMAX];
int h[NMAX] , flux[NMAX];
//int viz[NMAX] , pred[NMAX];
set < pair < int , int > > noduri;

void citire(){
    int x , y , z;
    fin >> n >> m;
    //cout << n << " " << m << '\n';
    for(int i=1;i<=m;i++){
        if(i<n-1)
        {
            noduri.insert({0,i});
        }
        fin >> x >> y >> z;
        //cout << x << " " << y << " " << z << '\n';
        cost[x][y] += z;
        graf[x].push_back(y);
        graf[y].push_back(x);
    }
}

void preflow(){
    h[0] = n-1;
    for(int i=0;i < graf[0].size();i++){
        int nv = graf[0][i];
        reziduri[0][nv] = cost[0][nv];
        //fluxul pe care il avem in nod
        noduri.erase({flux[nv],nv});
        flux[nv] += cost[0][nv];
        noduri.insert({flux[nv],nv});

        reziduri[nv][0] = -cost[0][nv];
    }
}

int main()
{
    citire();
    return 0;
}
