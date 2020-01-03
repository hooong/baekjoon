import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.StringTokenizer;

/**
 * 11052번 카드 구매하기
 */
public class Baeckjun11052 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int[] dp = new int[n+1];
        int[] p = new int[n+1];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i=1; i<=n; i++) {
            p[i] = Integer.parseInt(st.nextToken());
        }

        dp[1] = p[1];
        for (int i=2; i<=n; i++) {
            if (i%2==0) {
                dp[i] = p[i];
                for (int j=1; j<(i/2); j++) {
                    dp[i] = Math.max(dp[i],dp[j]+dp[i-j]);
                }
                dp[i] = Math.max(dp[i],2*dp[i/2]);
            } else {
                dp[i] = p[i];
                for (int j=1; j<=(i/2); j++) {
                    dp[i] = Math.max(dp[i],dp[j]+dp[i-j]);
                }
            }
        }

        System.out.println(dp[n]);
    }
}
