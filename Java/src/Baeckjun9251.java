import java.util.Scanner;

/**
 * 9251번 LCS
 */
public class Baeckjun9251 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s1,s2;

        s1 = sc.next();
        s2 = sc.next();

        int[][] dp = new int[s1.length()+1][s2.length()+1];

        for (int i=1; i<=s1.length(); i++) {
            for (int j=1; j<=s2.length(); j++) {
                if (s1.charAt(i-1) == s2.charAt(j-1)) {
                    dp[i][j] = dp[i-1][j-1] + 1;
                }
                else dp[i][j] = Math.max(dp[i][j-1],dp[i-1][j]);
            }
        }

        System.out.println(dp[s1.length()][s2.length()]);
    }
}
