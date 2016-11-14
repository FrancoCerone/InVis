package fanko.panel.test;

import java.awt.Color;

import org.junit.Test;

import fanko.panel.awt.AWTDialog;

public class DialogColorTest {

    @Test
    public void test() {
        AWTDialog d = new AWTDialog();

        for (int i = 0; i < 5000; i++) {

            d.setBackground(Color.BLACK);
            try {
                Thread.sleep(50);
            } catch (InterruptedException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }

        }
        System.out.println();
    }

}
