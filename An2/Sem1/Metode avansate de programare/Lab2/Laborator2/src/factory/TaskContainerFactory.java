//package ubb.scs.map.ir.seminar.taskrunner.factory;
package factory;

//import ubb.scs.map.ir.seminar.taskrunner.container.Container;
import container.Container;
//import ubb.scs.map.ir.seminar.taskrunner.container.QueueContainer;
import container.QueueContainer;
//import ubb.scs.map.ir.seminar.taskrunner.container.StackContainer;
import container.StackContainer;
//import ubb.scs.map.ir.seminar.taskrunner.container.Strategy;
import container.Strategy;

public class TaskContainerFactory implements Factory {
    private static TaskContainerFactory instance=null;
    //public static final TaskContainerFactory INSTANCE=new TaskContainerFactory();


    @Override
    public Container createContainer(Strategy strategy) {
        if(strategy== Strategy.LIFO)
            return new StackContainer();
        else
           return new QueueContainer();
    }

    private TaskContainerFactory() {
    }

    public static TaskContainerFactory getInstance(){
        if(instance==null)
            instance=new TaskContainerFactory();
        return instance;
    }
}
