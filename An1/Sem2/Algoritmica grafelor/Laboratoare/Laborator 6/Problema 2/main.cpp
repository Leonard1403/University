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

#include <bits/stdc++.h>

using namespace std;

const int NMAX = 1e3+5;

//const string file = "10";

//ifstream fin(file+"-in.txt");
//ofstream fout(file+"-out.txt");

string reading , couting;
int n , m , c;
int sum = 0;
vector < int > graf[NMAX];
int cost[NMAX][NMAX], reziduri[NMAX][NMAX];
int viz[NMAX] , pred[NMAX];
int fluxuri[NMAX];

void citire(){
    ifstream fin(reading);
    int x , y , z;
    fin >> n >> c >> m;
    //cout << c << '\n';
    //cout << n << " " << m << '\n';
    for(int i=1;i<=m;i++){
        fin >> x >> y >> z;
        //cout << x << " " << y << " " << z << '\n';
        cost[x][y] += z;
        graf[x].push_back(y);
        graf[y].push_back(x);
    }
    fin.close();
}

int bfs(int nod)
{
    //cout << "parcurgere\n";
    //memset(viz,0,sizeof(viz));
    //cout << nod << " ";
    for(int i=0;i<=n;i++)
        viz[i] = 0;
    queue < int > noduri;
    noduri.push(nod);
    viz[nod] = 1;
    while(!noduri.empty()){
        //cout << "looop" << '\n';

        //nod curent
        int nc = noduri.front();
        //cout << "nod_curent: " << nc << " | ";
        //in cazul in care nodul curent este
        //chiar nodul destinatie pe care dorim sa-l atingem
        //nu mai are rost sa-l vizitam, asa ca continuam
        //algoritmul

        //if(nc==n)continue;
        //cout << "nod_vecini: ";
        //incepem sa vizitam vecinii
        for(int i=0;i<graf[nc].size()&&nc!=(n-1);i++){
            //nod vecin
            int nv = graf[nc][i];
            //in cazul in care fluxul pe care il avem pe muchie este atins
            //adica nu mai putem sa trecem ceva prin flux , nu ne dorim sa-l parcurgem
            //asa ca ne continuam aventura in gasirea fluxului maxim
            if(reziduri[nc][nv]==cost[nc][nv]||viz[nv]==1)continue;
            //clasic
            //cout << nv << " ";
            viz[nv] = 1;
            noduri.push(nv);
            //ne dorim ca acest algoritm sa salveze si drumul inapoi
            //asa ca plasam cate o bucatica din noduri in vectorul nostru
            pred[nv] = nc;
        }
        //cout << '\n';

        //eliminam nodul din lista
        noduri.pop();
    }
    //returnam viz[n] deoarece
    //dorim sa stim daca am reusit
    //sa atingem nodul n adica nodul destinatie
    //cu parcurgerea bfs pe care am facut-o
    return viz[(n-1)];
}

int edmonds_karp(){
    //cum ziceam si in functia de bfs
    //atat timp cat putem sa ajungem la nodul nostru
    //algoritmul continua parcurgerea
    int noduri, fminim, flux;
    for(int j=0;j<c;j++){
        flux = 0;
        while(bfs(j)==1){
            //refacem traseul invers
                for(int i=0;i<graf[(n-1)].size();i++)
                {
                    int nc = graf[(n-1)][i];
                //in cazul in care vecinul este full
                //pe muchie , nu putem sa-l luam in calcul
                //pentru transport
                    if(cost[nc][(n-1)]==reziduri[nc][(n-1)]||viz[nc]==0)continue;
                    pred[(n-1)] = nc;
                    fminim = 550000005;
                    for(noduri = (n-1); noduri != j; noduri = pred[noduri]){
                        fminim = min(fminim,cost[pred[noduri]][noduri]-reziduri[pred[noduri]][noduri]);
                    }
                    if(fminim==0)continue;
                    for(noduri = (n-1); noduri != j; noduri = pred[noduri]){
                        reziduri[pred[noduri]][noduri] += fminim;
                        reziduri[noduri][pred[noduri]] -= fminim;
                    }
                    flux += fminim;
                }
        }
        //cout << flux << '\n';
        fluxuri[j] = flux;
        sum = flux + sum;
    }
    return 0;
}

int main(int argc , char** argv)
{
    reading = argv[1];
    couting = argv[2];
    citire();
    ofstream fout(couting);
    edmonds_karp();
    fout << sum << '\n';
    for(int i=0;i<c;i++)
        fout << fluxuri[i] << " ";
    fout.close();
    return 0;
}
