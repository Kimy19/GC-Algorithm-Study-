import java.util.Scanner;

class Solution {
	public static void main(String args[]) throws Exception {
		Scanner sc = new Scanner(System.in);
		for (int test = 1; test <= 10; test++) {
			int T;
			T = sc.nextInt();

			if (T < 4)
				System.out.println("#" + test + " " + 0);

			int[] answer = new int[T];
			int result = 0;

			// 데이터 입력
			for (int i = 0; i < T; i++) {
				answer[i] = sc.nextInt();
			}

			// 체크
			for (int i = 2; i < T - 2; i++) {
				if (answer[i] > answer[i - 1] && answer[i] > answer[i - 2] && 
						answer[i] > answer[i + 1] && answer[i] > answer[i + 2]) {

					result += answer[i] - max(answer[i - 1], answer[i - 2], answer[i + 1], answer[i + 2]);
				}
			}

			// 프린트
			System.out.println("#" + test + " " + result);
		}
		sc.close();
	}

	private static int max(int x, int y, int z, int k) {
		int maxV;

		maxV = (x > y) ? x : y;
		maxV = (maxV > z) ? maxV : z;
		maxV = (maxV > k) ? maxV : k;

		return maxV;
	}
}
