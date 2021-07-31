import java.util.Scanner;
import java.io.FileInputStream;

/*
   사용하는 클래스명이 Solution 이어야 하므로, 가급적 Solution.java 를 사용할 것을 권장합니다.
   이러한 상황에서도 동일하게 java Solution 명령으로 프로그램을 수행해볼 수 있습니다.
 */
class Solution
{
	public static void main(String args[]) throws Exception
	{
		//System.setIn(new FileInputStream("res/input.txt"));

		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();

		for(int test_case = 1; test_case <= T; test_case++) {
			int N = sc.nextInt();
            int M = sc.nextInt();
            
            int[] bits = new int[N];
            boolean answer = true;
            
            //나머지
            for(int i=0; i<N && M>0; i++) {
            	bits[i] = M % 2;
                M /= 2;
            }
            
            for(int x : bits) {
            	if(x != 1) {
                	answer = false;
                    break;
                }
            }
            
            if(answer)
            	System.out.println("#"+test_case+" ON");
            else
                System.out.println("#"+test_case+" OFF");
		}
	}
}
