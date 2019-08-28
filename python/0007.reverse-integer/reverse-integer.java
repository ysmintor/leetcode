public class Solution {
    public int reverse(int x) {
        boolean negtiveFlag = false;
        if (x < 0) {
            negtiveFlag = true;
            // reverse to postive number;
            x = -x;
        }

        char[] valueOfOrigin = String.valueOf(x).toCharArray();

        int len = valueOfOrigin.length;
        for (int i = 0; i < len / 2; i++) {
            // swap reverse order
            char temp = valueOfOrigin[i];
            valueOfOrigin[i] = valueOfOrigin[len - 1 - i];
            valueOfOrigin[len - 1 - i] = temp;
        }
        String positiveReversed = new String(valueOfOrigin);
        int result = 0;
        try {
            result = Integer.parseInt(negtiveFlag ? "-" + positiveReversed : positiveReversed);
        } catch (NumberFormatException ex) {
            result = 0;
        }
        return result;
    }
}