//package ubb.scs.map.ir.seminar.taskrunner;

//import ubb.scs.map.ir.seminar.taskrunner.container.Strategy;
import container.Strategy;

//import ubb.scs.map.ir.seminar.taskrunner.model.MessageTask;
import model.MessageTask;
import model.SortingTask;
//import model.Task;
//import ubb.scs.map.ir.seminar.taskrunner.runner.PrinterTaskRunner;
import runner.DelayTaskRunner;
import runner.PrinterTaskRunner;
//import ubb.scs.map.ir.seminar.taskrunner.runner.StrategyTaskRunner;
import runner.StrategyTaskRunner;
//import runner.DelayTaskRunner;

import java.time.LocalDateTime;

public class TestRunner {

    public static MessageTask[] createMessageTaskArray(){
        MessageTask t1=new MessageTask("1","Feedback lab1",
                "Ai obtinut 9.60","Gigi", "Ana", LocalDateTime.now());
        MessageTask t2=new MessageTask("2","Feedback lab1",
                "Ai obtinut 5.60","Gigi", "Ana", LocalDateTime.now());
        MessageTask t3=new MessageTask("3","Feedback lab3",
                "Ai obtinut 10","Gigi", "Ana", LocalDateTime.now());
        return new MessageTask[]{t1,t2,t3};
    }

    public static SortingTask[] createSortingTaskArray(){
        int[] array = new int[100];
        array[0] = 9;
        array[1] = 7;
        array[2] = 2;
        array[3] = 15;
        array[8] = 10;
        array[20] = 200;
        SortingTask s1=new SortingTask("1","Feedback lab1",
                "Ai obtinut 9.60","Gigi", "Ana", LocalDateTime.now(),"BubbleSort",array);
        return new SortingTask[]{s1};
    }

    public static void main(String[] args) {
        MessageTask[] l = createMessageTaskArray();
        StrategyTaskRunner runner;

        if(args[0].equals("FIFO")) {
            System.out.println("StrategyTaskRunner(FIFO): ");
            runner = new StrategyTaskRunner(Strategy.FIFO);
            runner.addTask(l[0]);
            runner.addTask(l[1]);
            runner.addTask(l[2]);
            runner.executeAll();
        }
        else if(args[0].equals("LIFO")) {
            System.out.println("StrategyTaskRunner(LIFO): ");
            runner = new StrategyTaskRunner(Strategy.LIFO);
            runner.addTask(l[0]);
            runner.addTask(l[1]);
            runner.addTask(l[2]);
            runner.executeAll();
        }
        else{
            System.out.println("StrategyTaskRunner(FIFO)(basic): ");
            runner = new StrategyTaskRunner(Strategy.FIFO);
            runner.addTask(l[0]);
            runner.addTask(l[1]);
            runner.addTask(l[2]);
            runner.executeAll();
        }

        System.out.println("PrinterTaskRunner: ");
        PrinterTaskRunner decorator = new PrinterTaskRunner(runner);
        runner.addTask(l[0]);
        runner.addTask(l[1]);
        runner.addTask(l[2]);
        decorator.executeAll();

        System.out.println("DelayTaskRunner: ");
        DelayTaskRunner decorator2 = new DelayTaskRunner(runner);
        DelayTaskRunner decorator3 = new DelayTaskRunner(decorator2);
        runner.addTask(l[0]);
        runner.addTask(l[1]);
        runner.addTask(l[2]);
        decorator2.executeAll();

        System.out.println("Sortare");
        SortingTask[] lista=createSortingTaskArray();
        lista[0].execute();
    }

}


