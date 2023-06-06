module aplicatie.roadrunner {
    requires javafx.controls;
    requires javafx.fxml;


    opens aplicatie.roadrunner to javafx.fxml;
    exports aplicatie.roadrunner;
}