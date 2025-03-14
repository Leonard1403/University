//package ubb.scs.map.ir.seminar.taskrunner.runner;
package runner;

//import ubb.scs.map.ir.seminar.taskrunner.model.Task;
import model.Task;

public abstract class AbstractTaskRunner implements TaskRunner {
    protected TaskRunner runner;

    public AbstractTaskRunner(TaskRunner runner) {
        this.runner = runner;
    }
//
//    @Override
//    public void executeOneTask() {
//        runner.executeOneTask();
//    }


    @Override
    public abstract void executeOneTask();

    @Override
    public void executeAll() {
        while (runner.hasTask())
            executeOneTask();
        //runner.executeOneTask();
    }

    @Override
    public void addTask(Task t) {
        runner.addTask(t);
    }

    @Override
    public boolean hasTask() {
        return runner.hasTask();
    }
}