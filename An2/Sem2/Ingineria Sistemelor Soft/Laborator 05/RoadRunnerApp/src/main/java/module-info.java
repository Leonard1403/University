module aplicatie.roadrunnerapp {
    requires javafx.controls;
    requires javafx.fxml;

    requires org.controlsfx.controls;
    requires com.dlsc.formsfx;
    requires org.kordamp.bootstrapfx.core;
    requires java.sql;
    requires org.hibernate.orm.core;

    opens aplicatie.roadrunnerapp to javafx.fxml;
    opens aplicatie.roadrunnerapp.model to javafx.fxml;
    opens aplicatie.roadrunnerapp.persistance to javafx.fxml;

    exports aplicatie.roadrunnerapp;
    exports aplicatie.roadrunnerapp.model;
    exports aplicatie.roadrunnerapp.persistance;
}