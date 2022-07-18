#include <iostream>
#include <fstream>
#include <vector>
#include <stack>

using namespace std;

//Hierholzer’s Algorithm

string reading , couting;
//ifstream f ("2-in.txt");
//ofstream g ("2-out.txt");

const int N_MAX = 100015;
const int M_MAX = 500015;

int n, m;
int from[M_MAX], to[M_MAX];
bool visited[M_MAX];

vector <int> G[N_MAX];
vector <int> path;

void Read()
{
    ifstream f(reading);
    f >> n >> m;
    for (int i = 1; i <= m; i++)
    {
        int x, y;
        f >> x >> y;
        G[x].push_back(i);
        G[y].push_back(i);

        from[i] = x;
        to[i] = y;
    }
}

bool IsCycle()
{
    for (int i = 0; i < n; i++)
    {
        if (G[i].size() % 2 == 1)
        {
            return false;
        }
    }
    return true;
}

void Euler(int start)
{
    stack <int> S;
    S.push(start);

    while (S.empty() == false)
    {
        int node = S.top();
        if (G[node].empty() == false)
        {
            int edge = G[node].back();
            G[node].pop_back();

            if (visited[edge] == false)
            {
                visited[edge] = true;
                if (to[edge] != node)
                {
                    S.push(to[edge]);
                }
                else
                {
                    S.push(from[edge]);
                }
            }
        }
        else
        {
            path.push_back(node);
            S.pop();
        }
    }
}

void Print()
{
    ofstream g(couting);
    unsigned int n = path.size() - 1;
    for (unsigned int i = 0; i < n; i++)
    {
        g << path[i] << " ";
    }
}

int main(int argc, char** argv)
{
    reading = argv[1];
    couting = argv[2];

    Read();

    if (IsCycle() == false)
    {
        ofstream g(couting);
        g << "-1";
    }
    else
    {
        Euler(0);
        Print();
    }
}
