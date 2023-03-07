//package ubb.scs.map.ir.seminar.taskrunner.factory;
package factory;

//import ubb.scs.map.ir.seminar.taskrunner.container.Container;
import container.Container;
//import ubb.scs.map.ir.seminar.taskrunner.container.Strategy;
import container.Strategy;

public interface Factory {
    Container createContainer(Strategy startegy);
}

