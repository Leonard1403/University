#define DEBUG       //comment when you have to disable all debug macros.
#define LOCAL
#define NDEBUG    //comment when all assert statements have to be disabled.
#include <iostream>
#include <cstring>
#include <sstream>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <bitset>
#include <climits>
#include <ctime>
#include <algorithm>
#include <functional>
#include <stack>
#include <queue>
#include <list>
#include <deque>
#include <sys/time.h>
#include <iomanip>
#include <cstdarg>
#include <utility> //std::pair
#include <cassert>
#define tr(c,i) for(typeof(c.begin()) i = (c).begin(); i != (c).end(); i++)
#define present(c,x) ((c).find(x) != (c).end())
#define all(x) x.begin(), x.end()
#define pb push_back
#define mp make_pair
#define log2(x) (log(x)/log(2))
#define ARRAY_SIZE(arr) (1[&arr]-arr)
#define INDEX(arr,elem)        (lower_bound(all(arr),elem)-arr.begin())
#define lld long long int
#define MOD 1000000007
#define gcd __gcd
#define equals(a,b) (a.compare(b)==0)    //for strings only
using namespace std;



struct Graph{
   lld numV;
   vector<lld> *adj;
   lld **flow, **cap, **cf, *height, *excess;
      inline void SET0(lld *array)
      {
         for(lld i=0;i<=numV;i++)
            array[i]=0;
      }
   Graph(lld _numV)
      {
         numV=_numV;
         lld i;
         /* allocating memory....*/
         flow = new lld*[numV+1];
         for(i=0;i<=numV;i++)
            flow[i] = new lld[numV+1], SET0(flow[i]);
         cap = new lld*[numV+1];
         for(i=0;i<=numV;i++)
            cap[i] = new lld[numV+1], SET0(cap[i]);
         cf = new lld*[numV+1];
         for(i=0;i<=numV;i++)
            cf[i] = new lld[numV+1], SET0(cf[i]);

         height = new lld[numV+1];
         excess = new lld[numV+1];
         SET0(height);
         SET0(excess);
         adj = new vector<lld>[numV+1];
      }
   void addEdge(lld u, lld v, lld uv)
      {
         adj[u].push_back(v);
         cap[u][v] = uv;
         cf[u][v] = uv;
      }

   void initialize_preflow(lld source)
      {
         lld i, v;
         height[source] = numV-1;

         tr(adj[source],it)
         {
            v = *it;
            flow[source][v] = cap[source][v];
            flow[v][source] = -cap[source][v];
            excess[v] += cap[source][v];
            excess[source] -=cap[source][v];
            cf[source][v] = cap[source][v]-flow[source][v];
            cf[v][source] = cap[v][source]-flow[v][source];
         }
      }
   void push(lld u, lld v)
      {
         lld push_val = min(cf[u][v], excess[u]);
         flow[u][v] += push_val;
         flow[v][u] = -flow[u][v];
         excess[u] -=push_val;
         excess[v] +=push_val;
         cf[u][v] = cap[u][v]-flow[u][v];
         cf[v][u] = cap[v][u]-flow[v][u];
      }
   lld max_flow(lld source, lld sink)
      {
         initialize_preflow(source);
         queue<lld> q;
         bool considered[numV+1];
         lld u, v, m, i;
         memset(considered, false, sizeof(considered));
         tr(adj[source], it)
         {
            v = *it;
            if(v!=sink)
            {
               q.push(v);
               considered[v] = true;
            }
         }
         bool flag;
         u = -1;
         while(!q.empty())
         {

            u = q.front();
            m = -1;
            for(i=0;i<adj[u].size() && excess[u]>0; i++)
            {

               v = adj[u][i];
               if(cf[u][v]>0)
               {
                  if(height[u]>height[v])
                  {
                     push(u,v);
                     if(!considered[v] && v!=sink && v!=source)
                     {
                        considered[v] = true;
                        q.push(v);
                     }
                  }
                  else if(m==-1) m = height[v];
                  else   m = min(m, height[v]);
               }
            }

            if(adj[u].empty()) {q.pop();continue;}
            if(excess[u]!=0) height[u] = m+1;
            else
            {
               q.pop();
               considered[u] = false;
            }
         }
         return excess[sink];
      }

};

template<class T>
inline void inputInt(T &n )
{
   n=0;
   T ch=getchar_unlocked();
     while( ch < '0' || ch > '9' )
      ch=getchar_unlocked();
      while(  ch >= '0' && ch <= '9' )
       n = (n<<3)+(n<<1) + ch-'0', ch=getchar_unlocked();
}

int main()
{
#ifdef LOCAL
   freopen("input.in","r",stdin);
#endif
   lld e,u,v,n,c;
   //cout<<"V:"<<endl;
   cin>>n>>e;

   Graph g(n);
   while(e--)
   {

      inputInt(u);
      inputInt(v);
      inputInt(c);
      if(u!=v)
      {
         if(g.cf[u][v])
            g.cf[u][v]=g.cf[v][u]=g.cap[u][v]=g.cap[v][u]+c;
         else g.addEdge(u,v,c);
      }
   }
   cout<<g.max_flow(1,n)<<endl;

}
