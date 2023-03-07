//package ubb.scs.map.ir.seminar.taskrunner.container;
package container;

//import ubb.scs.map.ir.seminar.taskrunner.model.Task;
import model.Task;

public class StackContainer extends SuperClassContainer implements Container {
//    private Task[] tasks;
//    private int size;

    public StackContainer()
    {
        super();
//        tasks=new Task[10];
//        size=0;
    }

    @Override
    public Task remove() {
        if (!isEmpty())
        {
            size--;
            return tasks[size];
        }
        return null;
    }

//    @Override
//    public void add(Task task) {
//        if (tasks.length==size)
//        {
//            Task[] t=new Task[tasks.length*2];
//            System.arraycopy( tasks, 0, t, 0, tasks.length );
//            tasks=t;
//        }
//        tasks[size]=task;
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
