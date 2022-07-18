#include <bits/stdc++.h>

using namespace std;

//ifstream fin("1-in.txt");

string intrare, iesire;

const int CMAX = 1e5+15;
const int oo = INT_MAX;

int n, nr, start;
int vecini[CMAX];
int pred[CMAX];

//set < pair < int , int > > frunze;

set < pair < int , int > > noduri;
vector < int > parcurs;

void citire(){
    ifstream fin(intrare);
    fin >> n;
    cout << n << '\n';
    for(int i=0;i<n;i++)
    {
        fin >> nr;
        cout << nr << " ";
        //cout << nr << " ";
        pred[i] = nr;
        if(pred[i]==-1){

            start = i;
        }
        else{
            vecini[pred[i]]++;
        }
    }
    cout << '\n';
    for(int i=0;i<n;i++)
        noduri.insert({vecini[i],i});
    fin.close();
}

void afisare()
{
    set < pair < int , int > > copie_noduri = noduri;
    while(!copie_noduri.empty()){
        int vecini = copie_noduri.begin()->first;
        int nod = copie_noduri.begin()->second;
        cout << "Nr vecini: " << vecini << " " << "Nod: " << nod << '\n';
        cout << "Parinte: " << pred[nod] << '\n';
        copie_noduri.erase(copie_noduri.begin());
    }
}

void solve(){
    while(!noduri.empty()){
        int nr_vecini = noduri.begin()->first;
        int nod = noduri.begin()->second;
        //parcurs.push_back(pred[nr_vecini]);
        noduri.erase({nr_vecini,nod});
        noduri.erase({vecini[pred[nod]],pred[nod]});
        vecini[pred[nod]]--;
        noduri.insert({vecini[pred[nod]],pred[nod]});
        //afisare();
        parcurs.push_back(pred[nod]);
        //cout << "Vector pred: " << pred[nod] << '\n';
        //cout << "Marimea vectorului: " << parcurs.size() << '\n';
        if(nr_vecini<0)
            return;
        //cout << '\n';
    }
    parcurs.pop_back();
    parcurs.pop_back();
    //cout << "Marimea vectorului: " << parcurs.size() << '\n';
}

void afisare_solve()
{
    ofstream fout(iesire);
    cout << "Afisare Prufer: " << '\n';
    fout << parcurs.size()-2 << '\n';
    for(int i=0;i<parcurs.size()-2;i++){
        cout << parcurs[i] << " ";
        fout << parcurs[i] << " ";
    }
    cout << '\n';
    fout.close();
}

int main(int argc,char *argv[])
{
    intrare = argv[1];
    iesire = argv[2];
    citire();
    //cout << intrare[0] << '\n';
    //cout << intrare << " " << iesire << '\n';
    //sort(noduri+0,noduri+1+n,cmp);
    //afisare();
    //cout << '\n';
    solve();
    afisare_solve();
    return 0;
}
