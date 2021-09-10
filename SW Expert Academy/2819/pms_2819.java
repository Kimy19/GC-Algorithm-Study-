import java.util.*;
import java.io.FileInputStream;

class Solution
{
    private static final int[] MP = {-1, 0, 1};
    public static void main(String args[]) throws Exception
    {
        //System.setIn(new FileInputStream("input.txt"));

        Scanner sc = new Scanner(System.in);
        int T;
        T=sc.nextInt();

        for(int test_case = 1; test_case <= T; test_case++)
        {
            /*입력*/
            int[][] board = new int[4][4];
            for(int i=0; i<4; i++)
                for(int j=0; j<4; j++)
                    board[i][j] = sc.nextInt();

            Set<String> set = new HashSet<>();
            /*시작위치*/
            for(int i=0; i<4; i++)
                for(int j=0; j<4; j++)
                    solve(set, board, i, j,  "");

            System.out.println("#"+test_case+" "+set.size());
        }
    }
    private static void solve(Set<String> set, int[][] board, int x,  int y, String num) {
        if(num.length() == 7) {
            set.add(num);
            return;
        }
        num += board[x][y];
        Stack<int[]> next = nextPoint(x, y);
        while(!next.isEmpty()) {
            int[] point = next.pop();
            solve(set, board, point[0], point[1], num);
        }
    }
    /*가능한 좌표 목록*/
    private static Stack<int[]> nextPoint(int x, int y) {
        Stack<int[]> next = new Stack<>();
        for(int i : MP) {
            if(x + i > 3 || x + i < 0) continue;
            for(int j : MP) {
                if(( y + j > 3 || y + j < 0) ||
                        ( i == 0 && j == 0) ||
                        ( i != 0 && j != 0));
                else next.add(new int[]{x+i, y+j});
            }
        }
        return next;
    }
}
