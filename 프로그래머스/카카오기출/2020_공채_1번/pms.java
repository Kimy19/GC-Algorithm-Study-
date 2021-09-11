public class Solution {
    public int solution(String s) {
        int min = s.length();
        for (int i = 1; i <= s.length() / 2; i++) {
            int length = compress(s, i).length();
            min = Math.min(min, length);
        }
        return min;
    }

    private String compress(String str, int i) {

        int count = 1;
        StringBuilder result = new StringBuilder();
        String pattern = "";

        for (int j = 0; j <= str.length() + i; j += i) {

            String curStr;

            if (j >= str.length()) {
                curStr = "";
            } else if (str.length() < j + i) {
                curStr = str.substring(j);
            } else {
                curStr = str.substring(j, j + i);
            }

            if (j != 0) {
                if (curStr.equals(pattern)) {
                    count++;
                } else if (count >= 2) {
                    result.append(count).append(pattern);
                    count = 1;
                } else {
                    result.append(pattern);
                }
            }
            pattern = curStr;
        }
        return result.toString();
    }
}
