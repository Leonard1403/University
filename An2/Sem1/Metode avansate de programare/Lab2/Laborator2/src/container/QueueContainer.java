//package ubb.scs.map.ir.seminar.taskrunner.container;
package container;

//import ubb.scs.map.ir.seminar.taskrunner.model.Task;
import model.Task;

//public class QueueContainer extends SuperClassContainer implements Container{
public class QueueContainer extends SuperClassContainer{

//    private Task[] tasks;
//    private int size;
    public QueueContainer(){
//        tasks = new Task[10];
//        size = 0;
        super();
    }
    @Override
    public Task remove() {
        if(!isEmpty()){
            Task remo = tasks[0];
            int i = 0;
            while(i<size){
                tasks[i] = tasks[i+1];
                i = i+1;
            }
            size--;
            return remo;
        }
        return null;
    }

//    @Override
//    public void add(Task task) {
//        if(tasks.length==size){
//            Task[] t= new Task[tasks.length*2];
//            System.arraycopy(tasks,0,t,0,tasks.length);
//            tasks=t;
//        }
//        tasks[size] = task;
//        size++;
//    }
//
//    @Override
//    public int size() {
//        return size;
//    }
//
//    @Override
//    public boolean isEmpty() {
//        return size==0;
//    }
}
