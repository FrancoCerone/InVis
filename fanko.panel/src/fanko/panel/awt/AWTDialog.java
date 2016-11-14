package fanko.panel.awt;

import java.awt.Color;
import java.awt.Dialog;
import java.awt.geom.RoundRectangle2D;

public class AWTDialog extends AbstractAWTDialog {

    private static final long serialVersionUID = 1L;



    public AWTDialog(int parseInt, int parseInt2) {
        initDialog(parseInt, parseInt2);
    }


    public AWTDialog() {
        initDialog();
    }


    @Override
    public void createAndShowGUI() {
        System.out.println("Starting dialog with size:" + dialogWitdh + "x" + dialogHeight);
        d1 = new Dialog(this);

        d1.setSize(dialogWitdh, dialogHeight);
        // Hide title bar and borders
        d1.setUndecorated(true);
        // Set background for dialog
        d1.setBackground(new Color(10));
        // Set d1 location relative to desktop
        // d1 appears at center of screen
        d1.setLocationRelativeTo(null);
        // Set some shape to d1
        RoundRectangle2D.Double r = new RoundRectangle2D.Double(0, 0, dialogWitdh, dialogHeight, 0, 0);
        // Set the rounded rectangle shape
        d1.setShape(r);
        d1.setVisible(true);
    }


    @Override
    public void flashWithColor(Color c) {
        d1.setBackground(c);

    }

    @Override
    public void setColor(Color c) {
        d1.setBackground(c);

    }


    public static void main(String args[]) {
        new AWTDialog();
    }


}
