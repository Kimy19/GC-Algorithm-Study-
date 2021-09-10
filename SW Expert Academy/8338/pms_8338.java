import java.util.*;
import java.io.FileInputStream;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		//System.setIn(new FileInputStream("res/input.txt"));

		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();

		for(int test_case = 1; test_case <= T; test_case++)
		{
			      /*입력*/
            int len = sc.nextInt();
            Deque<Integer> que = new ArrayDeque<>();
            for(int i=0; i<len; i++) que.addLast(sc.nextInt());
            
            /*계산*/
            while(que.size() > 1) {
                int n1 = que.removeFirst();
                int n2 = que.removeFirst();
                
            	  int ans = (n1 + n2 > n1 * n2)? (n1+n2) : (n1 * n2);
                que.addFirst(ans);
            }
            
            /*출력*/
            System.out.println("#"+test_case+" "+que.remove());
		}
	}
}
