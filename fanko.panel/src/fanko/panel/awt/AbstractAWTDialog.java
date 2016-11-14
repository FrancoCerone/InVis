package fanko.panel.awt;

import java.awt.Color;
import java.awt.Dialog;
import java.awt.Frame;

import fanko.panel.SizeScreenHelper;
import fanko.panel.IDialog;

public abstract class AbstractAWTDialog extends Frame implements IDialog {


    protected static final long serialVersionUID = 1L;

    public Dialog d1;
    public int dialogWitdh = SizeScreenHelper.getWidthScreenSize();
    public int dialogHeight = SizeScreenHelper.getHeightScreenSize();

    public void initDialog() {
        createAndShowGUI();
    }


    public void initDialog(int dialogWidth, int dialogHigth) {
        this.dialogWitdh = dialogWidth;
        this.dialogHeight = dialogHigth;
        createAndShowGUI();
    }

    public abstract void flashWithColor(Color c);

    public abstract void setColor(Color c);

    public abstract void createAndShowGUI();

}
