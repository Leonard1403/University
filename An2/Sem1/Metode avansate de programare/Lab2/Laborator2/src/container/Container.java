//package ubb.scs.map.ir.seminar.taskrunner.container;
package container;

//import ubb.scs.map.ir.seminar.taskrunner.model.Task;
import model.Task;

public interface Container {
    Task remove();
    void add(Task task);
    int size();
    boolean isEmpty();
}



