import java.util.Scanner;

public class Baeckjun9095 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        for(int i=0; i<t; i++) {
            int n = sc.nextInt();

            int dp[] = new int[n+1];

            for(int j=1; j<=n; j++) {
                if(j==1) dp[j] = 1;
                else if(j==2) dp[j] = 2;
                else if(j==3) dp[j] = dp[j-1] + dp[j-2] + 1;
                else dp[j] = dp[j-1] + dp[j-2] + dp[j-3];
            }

            System.out.println(dp[n]);
        }
        sc.close();
    }
}
