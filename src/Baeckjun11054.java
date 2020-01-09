import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 11054번 가장 긴 바이토닉 부분 수열
 */
public class Baeckjun11054 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int[][] dp = new int[n+1][2];
        int[] seq = new int[n+1];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i=1; i<=n; i++) {
            seq[i] = Integer.parseInt(st.nextToken());
        }

        int answer = 1;
        for (int i=1; i<=n; i++) {
            dp[i][0] = dp[i][1] = 1;
            for (int j=1; j<i; j++) {
                if (seq[j] < seq[i]) {
                    dp[i][0] = Math.max(dp[i][0],dp[j][0]+1);
                }
                else if (seq[j] > seq[i]) {
                    dp[i][1] = Math.max(dp[i][1],Math.max(dp[j][1]+1,dp[j][0]+1));
                }
            }
            answer = Math.max(answer,Math.max(dp[i][0],dp[i][1]));
        }

        System.out.println(answer);
    }
}
