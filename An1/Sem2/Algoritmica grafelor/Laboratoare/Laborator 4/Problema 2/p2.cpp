#include <bits/stdc++.h>

using namespace std;

//ifstream fin("1-in.txt");

string intrare, iesire;

const int CMAX = 1e5+15;
const int oo = INT_MAX;

bool exist[CMAX];
int n, nr, start;
int aparitii[CMAX];
int vecini[CMAX];

//int prufer[CMAX];

queue < int > prufer;

//set < pair < int , int > > frunze;

set < int > noduri;
set < pair < int , int > > in_list;

//prima este nr de aparitii
//a 2-a este noduri

set < int >::iterator it;

vector < int > parcurs;
int inceput, pred[CMAX];

void afisare_pred();
void afisare_inexistent();
void afisare_aparitii();

void citire(){
    ifstream fin(intrare);
    int nr;
    fin >> n;
    //cout << n << '\n';
    for(int i=1;i<=n+1;i++)
    {
        if(exist[i-1]==0){
            noduri.insert(i-1);
        }
        if(i!=n+1){
        fin >> nr;
        inceput = nr;
        prufer.push(nr);

        in_list.erase({aparitii[nr],nr});
        aparitii[nr]++;
        in_list.insert({aparitii[nr],nr});

        exist[nr] = 1;
        //cout << prufer[i] << " ";
        noduri.erase(nr);
        //afisare_inexistent();
        }
    }

    //cout << '\n';
}

void decodare_prufer(/*int prufer[],int n*/){
    /*
    in_list
    noduri
    */
    queue < int > copie;
    for(int i=1;i<=n;i++){

        //copie = prufer;

        //cout << "Elemente din codul prufer: ";
        //while(!copie.empty()){
        //    cout << copie.front() << " ";
        //    copie.pop();
        //}
        //cout << '\n';

        int nod_mic = *noduri.begin();
        pred[nod_mic] = prufer.front();
        //cout << "Cel mai mic nod care nu se afla in codul prufer: " << nod_mic << "\n";

        noduri.erase(nod_mic);
        //cout << "S-a sters cel mai mic element din lista de noduri\n";
        aparitii[nod_mic]++;
        in_list.insert({aparitii[nod_mic],nod_mic});
        prufer.push(nod_mic);
        //cout << "S-a adaugat in lista de aparitii Prufer\n";

        //cout << "Se modifica primul element din codul prufer pentru in_list\n";
        in_list.erase({aparitii[prufer.front()],prufer.front()});
        aparitii[prufer.front()]--;
        if(aparitii[prufer.front()]==0)
        {
            noduri.insert(prufer.front());
        }
        else
        {
            in_list.insert({aparitii[prufer.front()],prufer.front()});
        }

        prufer.pop();

        //cout << "NOU din codul prufer: ";
        //copie = prufer;

        //cout << "Elemente din codul prufer: ";
        //while(!copie.empty()){
        //    cout << copie.front() << " ";
        //    copie.pop();
        //}
        //cout << '\n';

        //afisare_pred();
        //afisare_aparitii();
        //afisare_inexistent();

        //cout << '\n';
    }
    pred[inceput] = -1;
}


void afisare_inexistent(){
    cout << "Noduri care nu se regasesc in codul prufer\n";
    set < int >::iterator it;
    for(it=noduri.begin();it!=noduri.end();++it){
        cout << *it << " ";
    }
    cout << '\n';
}

void afisare_pred(){
    cout << "Predecesori:\n";
    for(int i=0;i<=n;i++)
        cout << pred[i] << " ";
    cout << '\n';
}
void afisare_aparitii(){
    cout << "Noduri care se regasesc in codul prufer\n";
    set < pair < int , int > >::iterator it;
    for(it=in_list.begin();it!=in_list.end();++it)
        cout << "Aparitii: " << (*it).first << " Nod: " << (*it).second << '\n';
    cout << '\n';
}

void afisare(int afis[]){
    ofstream fout(iesire);
    fout << n+1 << '\n';
    for(int i=0;i<=n;i++)
        fout << afis[i] << " ";
    fout.close();
}

int main(int argc,char *argv[])
{

    intrare = argv[1];
    iesire = argv[2];

    /*
    intrare = "9-in.txt";
    iesire  = "9-out.txt";
    */

    citire();


    //cout << "Intrarea: \n";
    //afisare_inexistent();
    //afisare_aparitii();
    //cout << "Start: \n";

    decodare_prufer();
    afisare(pred);
    //afisare_inexistent();
    //afisare_aparitii();
    return 0;
}
