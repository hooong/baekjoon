import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 1912번 연속합
 */
public class Baeckjun1912 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;

        int n = Integer.parseInt(br.readLine());

        int[] seq = new int[n+1];
        int[] dp = new int[n+1];

        st = new StringTokenizer(br.readLine());
        for (int i=1; i<=n; i++) {
            seq[i] = Integer.parseInt(st.nextToken());
        }

        dp[1] = seq[1];
        int max = dp[1];
        for (int i=1; i<=n; i++) {
            dp[i] = Math.max(dp[i-1]+seq[i],seq[i]);

            max = Math.max(dp[i],max);
        }

        System.out.println(max);
    }
}
