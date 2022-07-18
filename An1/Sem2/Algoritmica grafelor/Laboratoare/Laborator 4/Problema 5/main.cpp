//Implementare algoritmul lui Kruskal

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

string reading;
string couting;


const int CMAX = 2e5+15;

set < pair < int , int >> Muchii_set;
vector < pair < int , int >> Graf[CMAX];
vector < pair < int , int >> Arbore;
vector < int > Padure[CMAX];
vector < pair < int , int >>Muchii_vector;
int viz[CMAX];
int n , m;
long long int cost_total;

void read(){
    ifstream fin(reading);
    int x , y , w;
    fin >> n >> m;
    Muchii_vector.push_back({0,0});
    viz[0] = 0;
    Padure[0].push_back(0);
    for(int i=1;i<=m;i++)
    {
        if(i<=n)
        {
            viz[i] = i;
            Padure[i].push_back(i);
        }
        fin >> x >> y >> w;
        Graf[x].push_back({y,w});
        Graf[y].push_back({x,w});
        Muchii_set.insert({w,i});
        Muchii_vector.push_back({x,y});
    }
    fin.close();
}

void kruskal(){
    int poz, cost;
    cost_total = 0;
    set < pair < int , int >>::iterator it;
    for(it = Muchii_set.begin();it!=Muchii_set.end();it++){
        //cout << (*it).first << " " << (*it).second << '\n';
        //cout << x << " " << y << '\n';
        //cout << '\n';

        cost = (*it).first;
        poz = (*it).second;

        int x = Muchii_vector[poz].first;
        int y = Muchii_vector[poz].second;
        //verificam daca unul din noduri nu este in padurea noastra
        //sau daca nodul pe care l-am gasit face parte dintr-o alta padure
        //in felul acesta putem sa colonizam o arie mai mare
        if(viz[x]!=viz[y]){
            cost_total = cost_total + cost;
            Arbore.push_back({x,y});
            int minimul = min(viz[x],viz[y]);
            int another = (-1)*(minimul-(viz[x]+viz[y]));
            int marime = Padure[another].size();

            viz[x] = minimul;
            viz[y] = minimul;

            //cout << "S-a produs schimbare intre padurile " << minimul << " " << another << '\n';

            while(!Padure[another].empty()){
                Padure[minimul].push_back(Padure[another][marime-1]);
                viz[Padure[another][marime-1]] = minimul;
                Padure[another].pop_back();
                marime = marime - 1;
            }

            /*
            for(int ji = 1; ji <= n; ji++)
            {
                cout << "Padurea " << ji << ": ";
                for(int jj = 0; jj < Padure[ji].size() ; jj++){
                    cout << Padure[ji][jj] << " ";
                }
                cout << '\n';
            }
            cout << '\n';
            */
        }
    }
}

void afisare(){
    ofstream fout(couting);
    fout << cost_total << '\n';
    int marime = Arbore.size();
    fout << marime << '\n';
    sort(Arbore.begin(),Arbore.end());
    for(int i=0;i<marime;i++)
    {
        fout << Arbore[i].first << " " << Arbore[i].second << '\n';
    }
    fout.close();
}

int main(int argc, char* argv[])
{
    reading = argv[1];
    couting = argv[2];
    read();
    kruskal();
    afisare();
    return 0;
}
