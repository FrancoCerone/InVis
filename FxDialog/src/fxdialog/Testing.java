package fxdialog;

import java.util.Date;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.layout.VBox;
import javafx.scene.paint.Color;
import javafx.stage.Stage;

final class Testing {

    private Button button = new Button();
    VBox vbox = new VBox();
    Scene scene = new Scene(vbox, 400, 400);
    static Testing testing;

    {
        button.setText(new Date().toString());
    }

    private Testing() {
        button.setOnAction(e -> {
            button.setText(new Date().toString());
        });
    }

    public static void main(String[] arArgs) {



        Utility.launchApp(new Utility.AppLaunch() {
            @Override
            public void start(Application app, Stage stage) throws Exception {

                testing = new Testing();

                stage.setWidth(300);
                stage.setHeight(300);

                Scene scene = testing.scene;
                stage.setScene(scene);
                scene.setFill(Color.BLACK);
                System.out.print(app.getParameters());

                stage.show();
            }

            @Override
            public void init(Application app) throws Exception {
                System.out.println("init");
            }

            @Override
            public void stop(Application app) throws Exception {
                System.out.println("stop");
            }
        }, arArgs);

        testing.scene.setFill(Color.BLACK);

    }

}
