import java.util.Scanner;
/**
 * 2156번 포도주 시식
 */

public class Baeckjun2156 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int[] w = new int[n+1];
        int[] dp = new int[n+1];

        for(int i=1; i<=n; i++) {
            w[i] = sc.nextInt();
        }

        for (int i=1; i<=n; i++) {
            if (i==1) dp[i] = w[1];
            else if (i==2) dp[i] = w[1] + w[2];
            else dp[i] = Math.max(dp[i-1], Math.max(dp[i-2]+w[i],dp[i-3]+w[i-1]+w[i]));
        }

        System.out.println(dp[n]);
    }
}
