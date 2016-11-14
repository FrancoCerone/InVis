package fanko.panel;

import java.awt.GraphicsDevice;
import java.awt.GraphicsEnvironment;

public class SizeScreenHelper {
    public static int getWidthScreenSize() {
        GraphicsDevice gd = GraphicsEnvironment.getLocalGraphicsEnvironment().getDefaultScreenDevice();
        int width = gd.getDisplayMode().getWidth();
        return width;
    }

    public static int getHeightScreenSize() {
        GraphicsDevice gd = GraphicsEnvironment.getLocalGraphicsEnvironment().getDefaultScreenDevice();
        int height = gd.getDisplayMode().getHeight();
        return height;
    }

    public static int getHalfWidthScreenSize() {
        return getWidthScreenSize() / 2;
    }

    public static int getHalfHeightScreenSize() {
        return getHeightScreenSize() / 2;
    }

}
