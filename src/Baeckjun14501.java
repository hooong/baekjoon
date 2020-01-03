import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

/**
 * 14501번 퇴사
 */
public class Baeckjun14501 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int[][] meets = new int[n+1][2];
        int[] dp = new int[n+1];

        StringTokenizer st = null;
        for (int i=1; i<=n; i++) {
            st = new StringTokenizer(br.readLine());
            meets[i][0] = Integer.parseInt(st.nextToken());
            meets[i][1] = Integer.parseInt(st.nextToken());
        }

        for (int i=1; i<=n; i++) {
            int max = dp[i];
            for (int j=1; j<=i; j++) {
                if ((i-j+1) == meets[j][0]) max = Math.max(max, dp[j-1]+meets[j][1]);
            }
            dp[i] = Math.max(dp[i-1], max);
        }
        System.out.println(dp[n]);
    }
}
