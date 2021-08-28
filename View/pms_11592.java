import java.util.Scanner;
import java.io.FileInputStream;

class Solution{
    public static void main(String args[]) throws Exception    {

        Scanner sc = new Scanner(System.in);
        int T=sc.nextInt();

        for(int test_case = 1; test_case <= T; test_case++)        {
            double d=sc.nextDouble();
            int n=sc.nextInt();
            double max=0;
            for(int i=0;i<n;i++){
                double k=sc.nextDouble();
                double s=sc.nextDouble();
                max=Math.max(max,(d-k)/s);
            }
            System.out.printf("#%d %.8f\n",test_case,d/max);
        }

        sc.close();
    }
}
