package service;

import domain.Friendship;
import domain.User;

import java.util.*;

/**
 * Network is a class for community operation
 * mat- matrix with integer values
 * size-integer(size of matrix)
 *ind-Set that contains Long keys
 */
public class Network {
    private final Integer[][] mat;
    private final Integer size;
    private final Set<Long> ind;

    /**
     * create a matrix of friends connections
     * @param size of matrix, number of users
     */
    public Network(int size) {
        this.ind = new HashSet<>();
        this.mat = new Integer[size][size];
        this.size = size;
        for (int i = 0; i < size; i++)
            for (int j = 0; j < size; j++)
                this.mat[i][j] = 0;
    }

    /**
     * add a friendships to the network
     * @param list-list of Friendships
     */
    public void addFriendships(Iterable<Friendship> list) {
        list.forEach(f ->
                this.mat[(int) (f.getId().getLeft() - 1)][(int) (f.getId().getRight() - 1)] = 1);
        list.forEach(f ->
                this.mat[(int) (f.getId().getRight() - 1)][(int) (f.getId().getLeft() - 1)] = 1);

    }

    /**
     * add users to the network
     * @param list- list of Users
     */
    public void addUsers(Iterable<User> list) {
        list.forEach(x -> ind.add(x.getId()-1));
    }

    /**
     * dfs algorithm
     * @param v-integer
     * @param visited-boolean array
     */
    private void DFSUtils(int v, boolean[] visited) {
        visited[v] = true;
        for (int i = 0; i < size; i++)
            if (mat[v][i] == 1 && !visited[i])
                DFSUtils(i, visited);
    }

    //V1.DFS
//    private int maxim1 = 0, nod1;
//
//    private void maximSet(){
//        maxim1 = 0;
//        nod1 = 0;
//    }
//
////    V1. DFS
//    private void DFSUtil(int v, boolean[] visited,int dist){
//        if(maxim1<dist){
//            maxim1 = dist;
//            nod1 = v;
//        }
//        visited[v] = true;
//        for(int i=0;i<size;i++)
//            if(mat[v][i]==1&& !visited[i]) {
//                DFSUtil(i, visited, dist + 1);
//            }
//    }
    private final List<Long> lista = new ArrayList<>();
    private final List<Long> listaDFS = new ArrayList<>();
    private int maxim1 = 0;

    private void DFSUtil(int v, boolean[] visited, int dist){
        listaDFS.add((long)v+1);
        if(maxim1<dist){
            lista.clear();
            lista.addAll(listaDFS);
            maxim1 = dist;
        }
        for(int i=0;i<size;i++){
            if(mat[v][i]==1 && !visited[i]){
                visited[v] = true;
//                listaDFS.add((long)i+1);
                DFSUtil(i, visited, dist+1);
//                listaDFS.remove((long)i+1);
                visited[v] = false;
            }
        }
        listaDFS.remove((long)v+1);
    }

    public List<Long> biggestComponent() {
        boolean[] visited = new boolean[size];
//        List<Long>listFinal=new ArrayList<>();
        for(int i=0;i<size;i++){
//            if(!visited[i]){
//                listFinal.clear();
//                listaDFS.add((long)i+1);
                DFSUtil(i, visited, 0);
//                listFinal.addAll(lista);
//                listaDFS.remove((long)i+1);
//            }
        }
        return lista;
    }
    /**
     * check how many connected Components we have
     * @return nr-integer (the result)
     */
    public int connectedComponents() {
        int nr = 0;
        boolean[] visited = new boolean[size];

        for (int i = 0; i < size; i++) {
            if (!visited[i]) {
                DFSUtils(i, visited);
                nr++;
            }
        }
        return nr;
    }

    /**
     * find the biggest Component
     * @return list of Integer(the result)
     */

//   V1.DFS
//    public List<Long> biggestComponent(){
//        boolean[] visited = new boolean[size];
//        boolean[] viz = new boolean[size];
//        List<Long>listFinal=new ArrayList<>();
//        int maxim=0;
//        for(int i=0;i<size;i++){
//            if(viz[i]==false&& ind.contains(Long.valueOf(i))) {
//                maximSet();
//                for (int j = 0; j < size; j++) {
//                    visited[j] = false;
//                }
//                DFSUtil(i, visited, 0);
//               for (int j = 0; j < size; j++) {
//                    visited[j] = false;
//                }
//                DFSUtil(nod1, visited, 0);
//                if (maxim < maxim1) {
////                      System.out.println(maxim1);
////                      System.out.println("Schimbat");
//                    listFinal.clear();
//                    maxim = maxim1;
//                    for(int j = 0;j<size;j++){
//                        if(visited[j]!=viz[j]&&viz[j]==false)
//                        {
//                            viz[j] = visited[j];
//                           listFinal.add((long) j+1);
//                        }
//                    }
//                }
//            }
//       }
//        return listFinal;
//    }

//    public List<Long> biggestComponent() {
//        boolean[] visited = new boolean[size];
//        boolean[] viz=new boolean[size];
//        List<Long>listFinal=new ArrayList<>();
//        int maxim=0;
//        for (int i = 0; i < size; i++)
//            if (!visited[i] && ind.contains(Long.valueOf(i))) {
//                DFSUtils(i, visited);
//                int nr=0;
//                List<Long>listForNow=new ArrayList<>();
//                for(int p=0;p<size;p++){
//                    if(visited[p]!=viz[p]){
//                        nr++;
//                        listForNow.add((long) p + 1);
//                        viz[p]=visited[p];
//                    }
//                    if(nr>maxim){
//                        listFinal.clear();
//                        listFinal.addAll(listForNow);
//                        maxim=nr;
//                    }
//                }
//            }
//        return listFinal;
//    }
}
