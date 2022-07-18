#include <bits/stdc++.h>

using namespace std;

//Euleristica simpla

ifstream fin("test.txt");
ofstream fout("test-out.txt");

const int CMAX = 1e2+15;
int n , m;

bool viz[CMAX];

vector < int > graph[CMAX];
int color[CMAX];
int c_min = 0;

void read(){
    int x , y ;
    fin >> n >> m;
    for(int i=1;i<=m;i++){
        fin >> x >> y;
        cout << x << " " << y << '\n';
        graph[x].push_back(y);
        graph[y].push_back(x);
        color[i] = CMAX;
    }
}

bool valid(int nod){
    cout << "nodul: " << nod << '\n';
    cout << "Colorare in progres: ";
    for(int i=0;i<n;i++)
        cout << color[i] << " ";
    cout << '\n';

    for(int i=0;i<graph[nod].size();i++){
        int nv = graph[nod][i];
        if(color[nv]==color[nod]){
            cout << "nu merge\n";
            cout << nv << " si " << nod << " au aceeasi culoare \n";
            return false;
        }
    }
    return true;
}

bool ok = 0;
int bkt(int nod,int nr){
    if(nr==n&&ok==0)
    {
        //cout << nr << " " << n << '\n';
        //cout << "intrat";
        cout << c_min << '\n';
        for(int i=0;i<n;i++)
            cout << color[i] << " ";
        cout << '\n';
        ok = 1;
        return 0;
    }
    else{
        cout << "Nod curent: " << nod << '\n';
        cout << "Color in Progress: ";
        for(int i=0;i<n;i++)
            cout << color[i] << " ";
        cout << '\n';
        for(int i=0;i<graph[nod].size()&&ok==0;i++){
            int nv = graph[nod][i];
            if(viz[nv]==0&&ok==0){
                for(int j=0;j<c_min&&ok==0;j++){
                    color[nv] = j;
                    if(valid(nv)==true&&ok==0)
                    {
                        viz[nv] = 1;
                        bkt(nv,nr+1);
                        viz[nv] = 0;
                    }
                }
                if(valid(nv)==false&&ok==0){
                    color[nv] = c_min;
                    c_min++;
                    viz[nv] = 1;
                    bkt(nv,nr+1);
                    viz[nv] = 0;
                }
            }
        }
    }
}

int main()
{
    read();
    color[0] = 0;
    viz[0] = 1;
    c_min = 1;
    bkt(0,1);
    return 0;
}
