package domain;

import java.util.Objects;

import static java.lang.Math.abs;

public class Pair<E1,E2> {
    private E1 e1;
    private E2 e2;

    public Pair(E1 e1, E2 e2) {
        this.e1 = e1;
        this.e2 = e2;
    }

    public E1 getLeft() {
        return e1;
    }
    public void setLeft(E1 e1) {
        this.e1 = e1;
    }

    public E2 getRight() {
        return e2;
    }
    public void setRight(E2 e2) {
        this.e2 = e2;
    }

    @Override
    public String toString() {
        return "" + e1 + "," + e2;
    }

    @Override
    public boolean equals(Object obj) {
        // after the hashcode is equal the program will check if its are equal
        Tuple that=(Tuple) obj;
        if(that.getLeft()==this.getRight() && this.getLeft()==that.getRight())
            return true;
        return this.e1.equals(((Pair) obj).e1) && this.e2.equals(((Pair) obj).e2);
    }

    @Override
    public int hashCode() {
        int hash = 17;
        //this is a nice hashcode
        //I thought about a type of hash code that will eliminate the case (1 2) ==(2 1)
        hash = hash * 23 + (e2.hashCode()+e1.hashCode());
        hash = hash * 23 + abs(e2.hashCode()-e1.hashCode());
        return hash;
    }
}
