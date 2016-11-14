package fxdialog;

import javafx.application.Application;
import javafx.beans.value.ObservableBooleanValue;
import javafx.scene.Scene;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.VBox;
import javafx.scene.paint.Color;
import javafx.stage.Stage;
import fanko.panel.IDialog;


public class FxDialog extends Application implements IDialog {

    private static FxDialog instance;
    Stage stage;
    VBox vbox;
    BorderPane root;
    ObservableBooleanValue a;
    private static final Color[] COLORS = new Color[] {Color.WHITE, Color.AQUA, Color.web("#FFDA8F"), Color.CORAL, Color.CYAN};

    public FxDialog() {
        instance = this;
    }

    public synchronized static FxDialog getInstance() {
        return instance;
    }


    @Override
    public void start(Stage primaryStage) throws Exception {
        root = new BorderPane();
        vbox = new VBox();
        root.setCenter(vbox);

        VBox vbox = new VBox();

        stage = primaryStage;

        Scene scene = new Scene(vbox, 400, 400);
        scene.setFill(Color.BLACK);
        stage.setScene(scene);
        stage.show();
    }


    @Override
    public void initDialog() {
        try {
            init();
        } catch (Exception e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        launch(null);

    }

    @Override
    public void flashWithColor(java.awt.Color c) {
        // TODO Auto-generated method stub

    }

    @Override
    public void setColor(java.awt.Color c) {

    }

    @Override
    public void createAndShowGUI() {

    }


    public static void main(String[] args) {
        FxDialog d = new FxDialog();
        d.initDialog();
        d.setColor(null);



    }
}
