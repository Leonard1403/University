//package ubb.scs.map.ir.seminar.taskrunner.runner;
package runner;

//import ubb.scs.map.ir.seminar.taskrunner.container.Container;
import container.Container;
//import ubb.scs.map.ir.seminar.taskrunner.container.Strategy;
import container.Strategy;
//import ubb.scs.map.ir.seminar.taskrunner.factory.TaskContainerFactory;
import factory.TaskContainerFactory;
//import ubb.scs.map.ir.seminar.taskrunner.model.Task;
import model.Task;

public class StrategyTaskRunner implements TaskRunner {
    private Container container;
    //private Container container_copie;
    @Override
    public void executeOneTask() {
        if (!container.isEmpty()) {
            container.remove().execute();
//            container.execute();
        }
    }

    @Override
    public void executeAll() {
        while (!container.isEmpty())
            executeOneTask();
    }

    @Override
    public void addTask(Task t) {
        container.add(t);
    }

    public StrategyTaskRunner(Strategy strategy) {
        this.container = TaskContainerFactory.getInstance().createContainer(strategy);
        //this.container_copie = TaskContainerFactory.getInstance().createContainer(strategy);
    }

    @Override
    public boolean hasTask() {
        return !container.isEmpty();
    }
}
