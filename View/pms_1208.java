import java.util.*;

class Solution
{
    public static void main(String args[]) throws Exception
    {
        Scanner sc = new Scanner(System.in);

        for(int test_case = 1; test_case <= 10; test_case++)
        {
            int cnt = sc.nextInt();
            int[] board = new int[100];
            for(int i=0; i<100; i++) board[i] = (sc.nextInt());

            Arrays.sort(board);

            for(int j=0; j<cnt; j++) {
                board[0]++;
                board[99]--;
                Arrays.sort(board);
            }

            System.out.println("#"+test_case+" "+(board[99] - board[0]));
        }
    }
}
