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
//Pompare preflex
#include <bits/stdc++.h>
using namespace std;

ifstream fin("9-in.txt");
ofstream fout("9-out.txt");

struct Edge
{
    int flow, capacity;

    int u, v;

    Edge(int flow, int capacity, int u, int v)
    {
        this->flow = flow;
        this->capacity = capacity;
        this->u = u;
        this->v = v;
    }
};

struct Vertex
{
    int h, e_flow;

    Vertex(int h, int e_flow)
    {
        this->h = h;
        this->e_flow = e_flow;
    }
};

class Graph
{
    int V;
    vector<Vertex> ver;
    vector<Edge> edge;

    bool push(int u);

    void relabel(int u);

    void preflow(int s);

    void updateReverseEdgeFlow(int i, int flow);

public:
    Graph(int V);
    void addEdge(int u, int v, int w);

    int getMaxFlow(int s, int t);
};

Graph::Graph(int V)
{
    this->V = V;

    for (int i = 0; i < V; i++)
        ver.push_back(Vertex(0, 0));
}

void Graph::addEdge(int u, int v, int capacity)
{
    edge.push_back(Edge(0, capacity, u, v));
}

void Graph::preflow(int s)
{
    ver[s].h = ver.size();


    for (int i = 0; i < edge.size(); i++)
    {
        if (edge[i].u == s)
        {
            edge[i].flow = edge[i].capacity;

            ver[edge[i].v].e_flow += edge[i].flow;

            edge.push_back(Edge(-edge[i].flow, 0, edge[i].v, s));
        }
    }
}

int overFlowVertex(vector<Vertex>& ver)
{
    for (int i = 1; i < ver.size() - 1; i++)
       if (ver[i].e_flow > 0)
            return i;

    return -1;
}

void Graph::updateReverseEdgeFlow(int i, int flow)
{
    int u = edge[i].v, v = edge[i].u;

    for (int j = 0; j < edge.size(); j++)
    {
        if (edge[j].v == v && edge[j].u == u)
        {
            edge[j].flow -= flow;
            return;
        }
    }

    Edge e = Edge(0, flow, u, v);
    edge.push_back(e);
}

bool Graph::push(int u)
{
    for (int i = 0; i < edge.size(); i++)
    {
        if (edge[i].u == u)
        {
            if (edge[i].flow == edge[i].capacity)
                continue;

            if (ver[u].h > ver[edge[i].v].h)
            {
                int flow = min(edge[i].capacity - edge[i].flow,
                               ver[u].e_flow);

                ver[u].e_flow -= flow;

                ver[edge[i].v].e_flow += flow;

                edge[i].flow += flow;

                updateReverseEdgeFlow(i, flow);

                return true;
            }
        }
    }
    return false;
}

void Graph::relabel(int u)
{
    int mh = INT_MAX;

    for (int i = 0; i < edge.size(); i++)
    {
        if (edge[i].u == u)
        {
           if (edge[i].flow == edge[i].capacity)
                continue;

            if (ver[edge[i].v].h < mh)
            {
                mh = ver[edge[i].v].h;

                ver[u].h = mh + 1;
            }
        }
    }
}

int Graph::getMaxFlow(int s, int t)
{
    preflow(s);

    while (overFlowVertex(ver) != -1)
    {
        int u = overFlowVertex(ver);
        if (!push(u))
            relabel(u);
    }

    return ver.back().e_flow;
}
string reading , couting;
int main(int argc , char** argv)
{
    reading = argv[1];
    couting = argv[2];
    int n , m;

    ifstream fin(reading);
    fin >> n >> m;
    Graph g(n);
    for(int i=1;i<=m;i++)
    {
        int x , y , z;
        fin >> x >> y >> z;
        g.addEdge(x,y,z);
    }
    fin.close();
    int s = 0, t = n- 1;
    ofstream fout(couting);
    fout << g.getMaxFlow(s,t);
    fout.close();
    return 0;
}
