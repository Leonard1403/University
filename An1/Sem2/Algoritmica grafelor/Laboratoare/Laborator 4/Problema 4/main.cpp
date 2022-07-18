#include <bits/stdc++.h>

using namespace std;

string reading;
string couting;

//ifstream fin(reading);
//ofstream fout(couting);

const int CMAX = 2e6+15;;

set < pair < int , int > > coding;
int length, contorizare[CMAX];

int n, stop;
int fr[CMAX];

long long temp;
struct noduri{
    int st, dr , niv;
    long long val;
    string codare;
}heap[CMAX];

char spatiu;
char litere[CMAX];
char dictionar[CMAX];

string text;
int lungime_text;

void read_adap(){
    //Functie de citire a textului dat
    ifstream fin(reading);
    /*
    fin >> noskipws;
    char cr;
    lungime_text = 0;

    while(fin >> cr){
        text = text + cr;
        lungime_text++;


        coding.erase({contorizare[(int)cr],cr});
        contorizare[(int)cr]++;
        coding.insert({contorizare[(int)cr],cr});
    }
    */
    fin >> n;
    int i = 1;
    char linie[CMAX];

    fin.getline(linie,10);
    while(i<=n){
        fin.getline(linie,10);
        //cout << linie << '\n';

        int j = 2;
        fr[i] = 0;
        while(linie[j]>='0'&&linie[j]<='9'){
            fr[i] = fr[i]*10 + linie[j] - 48;
            j++;
        }
        litere[i] = linie[0];
        //cout << fr[i] << " " << litere[i] << '\n';
        coding.insert({fr[i],litere[i]});
        i++;
    }
    fin >> text;
    cout << text << '\n';
    //cout << text << '\n';
    lungime_text = text.size();
    fin.close();
}

void afisare_adap(){
    //Functie de afisare si convertire la un dictionar
    //pentru utilizarea functiei huffman
    int i = 1;
    cout << n << '\n';
    //n = coding.size();
    while(!coding.empty()){
        heap[i].val = (*coding.begin()).first;
        litere[i] = (char)(*coding.begin()).second;
        fr[i] = heap[i].val;

        cout << i << ": ";
        cout << (*coding.begin()).first << " " << (char)(*coding.begin()).second << '\n';
        coding.erase(coding.begin());
        i++;
    }
    cout << '\n';
}

void convert(){
    int i = 1;
    //cout << '\n';
    while(i<=n){
        //cout << i << ": ";
        //cout << "Litera: " << litere[i] << " Codare: " << heap[i].codare << '\n';
        //dictionar[litere[i]] = heap[i].codare;
        cout << litere[i] << " " << dictionar[litere[i]] << '\n';
        i++;
    }
}

void afisare_codare_adap(){
    int i = 1;
    cout << '\n';
    while(i<=n){
        cout << i << ": ";
        cout << "Litera: " << litere[i] << " Codare: " << heap[i].codare << '\n';
        i++;
    }
    cout << '\n';
}

/*
void read(){
    fin >> n;
    //cout << n << '\n';
    for(int i=1;i<=n;i++)
    {
        fin >> heap[i].val;
        //cout << heap[i].val << '\n';
    }
}
*/

void parc_srd(int nod,int niv, long long val,string cod){
    if(nod>0){
    //cout << heap[nod].val << " " << nod << " " << val << '\n';
    heap[nod].val = val;
    heap[nod].niv = niv;
    heap[nod].codare = cod;
    parc_srd(heap[nod].st,niv+1,val*2,cod+"0");
    parc_srd(heap[nod].dr,niv+1,(val*2)+1,cod+"1");
    }
}

void afisare_struct(int stop){
    //cout << "Intrat";

    for(int i=1;i<=stop;i++){
        cout << i << ": ";
        cout << "Stanga: " << heap[i].st << " Dreapta: " << heap[i].dr << " Nivelul: " << heap[i].niv << " Valoarea: " << heap[i].val << '\n';
    }
}

void huffman(){
    heap[n+1].val = LONG_LONG_MAX;
    int i, j, st , dr;
    i = 1;
    j = n+2;
    stop = n+1;
    while(i < n+1 || j < stop){
        if(j <= stop && heap[j].val <= heap[i].val)
                st = j++;
        else{
            st = i++;
        }
        if(j <= stop && heap[j].val <= heap[i].val){
            dr = j++;
        }
        else
        {
            dr = i++;
        }
        heap[++stop].val = heap[st].val + heap[dr].val;
        heap[stop].st = st;
        heap[stop].dr = dr;
        //heap[stop].niv = max(heap[heap[stop].st].val,heap[heap[stop].dr].val) + 1;
        temp = temp + heap[stop].val;
    }
    //Afisare structura formata
    //afisare_struct(stop);
    //parc_srd(stop,0,0,"");
}

void traducere(){
    //Functia de traducere converteste textul nostru in
    //codul binar format din codarea huffman
    ofstream fout(couting);

    /*
    fout << n << '\n';
    for(int i=1;i<=n;i++)
    {
        fout << (char)litere[i] << " " << fr[i] << '\n';
    }
    */
    int i=0;
    int nod = stop;
    while(i<lungime_text){
        //cout << text[i] << " ";
        if(text[i]=='0'){
            //cout << "Stanga: ";
            //cout << heap[nod].st;
            //cout << '\n';

            nod = heap[nod].st;
            if(heap[nod].dr==0){
                fout << (char)litere[nod];
                nod = stop;
            }
        }
        else if(text[i]=='1'){
            //cout << "Dreapta: ";
            //cout << heap[nod].dr;
            //cout << '\n';

            nod = heap[nod].dr;
            if(heap[nod].dr==0){
                fout << (char)litere[nod];
                nod = stop;
            }
        }
        i++;
    }
    fout.close();
}

int main(int argc, char* argv[])
{
    /*
    //part banala
    read();
    huffman();
    fout << temp << '\n';
    for(int i=1;i<=n;i++)
    {
        fout << heap[i].niv << " " << heap[i].val << '\n';
    }
    */

    //part problemei noastre

    reading = argv[1];
    couting = argv[2];

    read_adap();
    //cout << text << '\n';
    //cout << "START PROGRAM\n";
    afisare_adap();
    huffman();
    //convert();
    afisare_struct(stop);
    traducere();
    //afisare_codare_adap();
    return 0;
}
