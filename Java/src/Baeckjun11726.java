import java.util.Scanner;
/**
 * 11726번 2xn타일링
 */

public class Baeckjun11726 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int dp[] = new int[n+1];

        for (int i=1; i<=n; i++) {
            if (i==1) dp[i] = 1;
            else if (i==2) dp[i] = 2;
            else dp[i] = (dp[i-2] + dp[i-1]) % 10007 ;
        }

        System.out.println(dp[n]);
    }
}
