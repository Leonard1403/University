//A IESIT
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
#include<bits/stdc++.h>

using namespace std;
ifstream fin("1.txt");
ofstream fout("colorare.out");

const int CMAX = 1e3+15;
int n , m;
int x , y;
int k = 0;
int found = 0;
int nr_min;
int culoare[CMAX];
int nr_min_gasit;
int ecolor;
bool viz[CMAX];
vector < int > G[CMAX];

void set_color(int nod){
    int ok = 1;
    //cout << "Cautam culoarea pentru nodul " << nod << '\n';
    for(int i=1;i<=nr_min;i++)
    {
        culoare[nod] = i;
        //cout << "Incercam sa punem colorarea " << i << '\n';
        ok = 0;
        for(int j=0;j<G[nod].size();j++)
        {
            int nv = G[nod][j];
            if(culoare[nod]==culoare[nv]){
                //cout << "Culoarea " << i << " nu putem sa o punem deoarece se aseamana cu culoarea nodului " << nv << '\n';
                ok = 1;
                break;
            }
        }
        if(ok==0)
            break;
    }
    if(ok==1){
        //cout << "Nu am gasit o culoare valabila asa ca il coloram cu " << nr_min + 1 << '\n';
        nr_min++;
        culoare[nod] = nr_min;
        return;
    }
    //cout << "Nodul poate fi colorat cu " << culoare[nod] << '\n';
}

void bkt(int nod){

    viz[nod] = 1;
    ecolor = ecolor + 1;
    set_color(nod);
    //cout << "Am colorat pana acum: " << ecolor << " noduri\n";
    //cout << '\n';

    if(ecolor == n && found == 0){
        //cout << "INTRAT\n";
        found = 1;
        //cout << nr_min << '\n';
        //nr_min_gasit = nr_min;
        //found = 1;
        //for(int i=0;i<n;i++)
        //    cout << culoare[i]-1 << " ";
        //cout << '\n';
        //return;
    }

    for(int i=0;i<G[nod].size();i++)
    {
        int nv = G[nod][i];
        if(viz[nv]==0)
            bkt(nv);
    }
    ecolor = ecolor - 1;
    viz[nod] = 0;

}

int main(){
    fin >> n >> m;
    for(int i=1;i<=m;i++)
    {
        fin >> x >> y;
        G[x].push_back(y);
        G[y].push_back(x);
        //cout << x << " " << y << '\n';
    }
    for(int i=0;i<n;i++)
        culoare[i] = -1;
    //culoare[0] = 1;
    ecolor = 0;
    nr_min = 0;
    bkt(0);

    cout << nr_min << '\n';
    for(int i=0;i<n;i++)
        cout << culoare[i]-1 << " ";
    return 0;
}

