import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 11053번 가장 긴 증가하는 부분 수열
 */
public class Baeckjun11053 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        int[] dp = new int[n+1];
        int[] seq = new int[n+1];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i=1; i<=n; i++) {
            seq[i] = Integer.parseInt(st.nextToken());
        }

        int answer = 1;
        for (int i=1; i<=n; i++) {
            dp[i] = 1;
            for (int j=1; j<=i; j++) {
                if (seq[i] > seq[j]) dp[i] = Math.max(dp[i],dp[j]+1);
            }
            answer = Math.max(answer,dp[i]);
        }
        System.out.println(answer);

    }
}
