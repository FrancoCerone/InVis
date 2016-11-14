import java.awt.Color;
import java.net.SocketException;
import java.util.Date;

import com.illposed.osc.OSCListener;
import com.illposed.osc.OSCMessage;
import com.illposed.osc.OSCPortIn;

import fanko.panel.IDialog;
import fanko.panel.awt.AWTDialog;


public class Receiver {
    IDialog awtDialog;

    public Receiver(String width, String height) {
        if (Integer.parseInt(width) != 0 && Integer.parseInt(height) != 0) {
            awtDialog = new AWTDialog(Integer.parseInt(width), Integer.parseInt(height));
        } else {
            awtDialog = new AWTDialog();
        }

        init();
    }

    private void init() {
        try {
            OSCPortIn receiver = new OSCPortIn(57110);


            OSCListener handler1 = new OSCListener() {
                public void acceptMessage(java.util.Date time, OSCMessage message) {
                    // TODO: Put your code to process a message in here
                    System.out.println("Handler1 called with address " + message.getAddress());

                    // Print out values
                    Object[] values = message.getArguments();
                    System.out.printf("Values: [%s", values[0]);
                    for (int i = 1; i < values.length; i++) {
                        System.out.printf(", %s", values[i]);
                    }

                    System.out.println("]\n");
                    if ((Integer) values[0] == 1) {
                        awtDialog.flashWithColor(Color.WHITE);
                    }
                    if ((Integer) values[0] == 0) {
                        awtDialog.setColor(Color.BLACK);
                    }



                }
            };
            receiver.addListener("/s_new", handler1);// "/message/receiving"
            receiver.startListening();
            // A second message handler



            OSCListener listener = new OSCListener() {
                public void acceptMessage(Date time, OSCMessage message) {
                    System.out.println("Message received!");
                }
            };
            receiver.addListener("javaosc-example", listener);
            receiver.startListening();
        } catch (SocketException e) {

        }

    }


    public static void main(String[] args) {
        System.out.println("Startin reciever");
        Receiver r;
        if (args.length == 2) {
            String width = args[0];
            String height = args[1];
            r = new Receiver(width, height);
        } else {
            r = new Receiver("0", "0");
        }

        System.out.println(r.toString());
    }



}
