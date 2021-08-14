import java.util.Scanner;
import java.io.FileInputStream;

class Solution {
    public static void main(String args[]) throws Exception {
        //System.setIn(new FileInputStream("input.txt"));

        Scanner sc = new Scanner(System.in);
        int T;
        T=sc.nextInt();
        for(int test_case = 1; test_case <= T; test_case++) {

            /*입력*/
            int len = sc.nextInt();
            int[] arr = new int[len];
            for(int i=0; i<len; i++) arr[i] = sc.nextInt();

            /*최대값*/
            int first = 0;
            int last = len-1;
            long ans = 0;

            while(first < last) {
                int maxIdx = getMaxIdx(arr, first, last);
                int max = arr[maxIdx];
                for(int i=first; i<maxIdx; i++) ans += max - arr[i];
                first = maxIdx + 1;
            }

            System.out.println("#"+test_case+" "+ans);
        }
    }

    private static int getMaxIdx(int[] arr, int first, int last) {
        int result = first;
        int max = arr[first];
        for(int i=first; i<=last; i++) {
            if(max < arr[i]) {
                max = arr[i];
                result = i;
            }
        }
        return result;
    }
}
